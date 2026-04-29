import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
from typing import Dict, Tuple

# ============================================================
# Configuração do Streamlit
# ============================================================

st.set_page_config(page_title="Moody's Rating Methodology", layout="wide")

# ============================================================
# Thresholds e Constantes (da metodologia Moody's)
# ============================================================

# Economic Strength Thresholds
GDP_GROWTH_THRESHOLDS = {
    ">4.50": "aaa",
    "4.50-4.40": "aa1",
    "4.40-3.70": "aa2",
    "3.70-3.30": "aa3",
    "3.30-3.00": "a1",
    "3.00-2.70": "a2",
    "2.70-2.40": "a3",
    "2.40-2.10": "baa1",
    "2.10-1.80": "baa2",
    "1.80-1.60": "baa3",
    "1.60-1.30": "ba1",
    "1.30-1.10": "ba2",
    "1.10-0.90": "ba3",
    "0.90-0.70": "b1",
    "0.70-0.50": "b2",
    "0.50-0.30": "b3",
    "<0.30": "caa"
}

MAD_VOLATILITY_THRESHOLDS = {
    "<0.3": "aaa",
    "0.3-0.5": "aa",
    "0.5-0.7": "a",
    "0.7-0.9": "baa",
    "0.9-1.1": "ba",
    "1.1-1.3": "b",
    ">1.3": "caa"
}

SCALE_ECONOMY_THRESHOLDS = {
    ">48,000": "aaa",
    "42,000-48,000": "aa1",
    "37,000-42,000": "aa2",
    "32,000-37,000": "aa3",
    "27,500-32,000": "a1",
    "24,500-27,500": "a2",
    "21,000-24,500": "a3",
    "19,000-21,000": "baa1",
    "16,000-19,000": "baa2",
    "14,000-16,000": "baa3",
    "12,000-14,000": "ba1",
    "10,750-12,000": "ba2",
    "9,500-10,750": "ba3",
    "8,000-9,500": "b1",
    "7,000-8,000": "b2",
    "6,200-7,000": "b3",
    "<6,200": "caa"
}

RATING_SCALE = [
    "aaa", "aa1", "aa2", "aa3", "a1", "a2", "a3",
    "baa1", "baa2", "baa3", "ba1", "ba2", "ba3",
    "b1", "b2", "b3", "caa1", "caa2", "caa3", "ca", "c"
]

# ============================================================
# Funções auxiliares
# ============================================================

def find_rating_from_value(value: float, thresholds_ranges: Dict) -> str:
    """Encontra o rating baseado em um valor e thresholds"""
    for range_key, rating in thresholds_ranges.items():
        if "-" in range_key:
            parts = range_key.split("-")
            min_val = float(parts[0].replace(",", ""))
            max_val = float(parts[1].replace(",", ""))
            if min_val <= value < max_val:
                return rating
        elif ">" in range_key:
            min_val = float(range_key.replace(">", "").replace(",", ""))
            if value > min_val:
                return rating
        elif "<" in range_key:
            max_val = float(range_key.replace("<", "").replace(",", ""))
            if value < max_val:
                return rating
    return "b3"

def rating_to_numeric(rating: str) -> float:
    """Converte rating para valor numérico (para média)"""
    return float(RATING_SCALE.index(rating.lower()))

def numeric_to_rating(numeric_val: float) -> str:
    """Converte valor numérico para rating"""
    idx = int(round(numeric_val))
    idx = max(0, min(len(RATING_SCALE) - 1, idx))
    return RATING_SCALE[idx]

def get_wgi_score_category(wgi_score: float) -> str:
    """Classifica score WGI para Institutions"""
    if wgi_score > 1.5:
        return "aaa"
    elif wgi_score > 1.0:
        return "aa"
    elif wgi_score > 0.5:
        return "a"
    elif wgi_score > 0.0:
        return "baa"
    elif wgi_score > -0.5:
        return "ba"
    elif wgi_score > -1.0:
        return "b"
    elif wgi_score > -1.5:
        return "caa"
    else:
        return "ca"

# ============================================================
# Funções de cálculo dos fatores
# ============================================================

def calculate_economic_strength(
    gdp_growth: float,
    mad_volatility: float,
    gdp_per_capita_ppp: float,
    nominal_gdp_bn: float
) -> Tuple[str, Dict]:
    """Calcula Economic Strength"""

    scores = {}

    # Growth Dynamics
    growth_score = find_rating_from_value(gdp_growth, GDP_GROWTH_THRESHOLDS)
    scores['growth'] = growth_score

    # MAD Volatility
    volatility_score = find_rating_from_value(mad_volatility, MAD_VOLATILITY_THRESHOLDS)
    scores['volatility'] = volatility_score

    # Scale of Economy
    scale_score = find_rating_from_value(gdp_per_capita_ppp, SCALE_ECONOMY_THRESHOLDS)
    scores['scale'] = scale_score

    # Agregação simples (média dos três)
    growth_numeric = rating_to_numeric(growth_score)
    volatility_numeric = rating_to_numeric(volatility_score)
    scale_numeric = rating_to_numeric(scale_score)

    avg_numeric = (growth_numeric * 0.30 + volatility_numeric * 0.35 + scale_numeric * 0.35)
    final_score = numeric_to_rating(avg_numeric)

    return final_score, scores

def calculate_institutions_governance(
    wgi_govt_effectiveness: float,
    wgi_regulatory_quality: float,
    wgi_voice_accountability: float,
    data_quality: float  # 1-10
) -> Tuple[str, Dict]:
    """Calcula Institutions and Governance Strength"""

    scores = {}

    # Quality of Legislative/Executive Institutions
    wgi_avg = (wgi_govt_effectiveness + wgi_regulatory_quality) / 2
    legislative_score = get_wgi_score_category(wgi_avg)
    scores['legislative'] = legislative_score

    # Quality of the Judiciary
    if wgi_voice_accountability > 1.0:
        judiciary_score = "aa"
    elif wgi_voice_accountability > 0.0:
        judiciary_score = "a"
    else:
        judiciary_score = "baa"
    scores['judiciary'] = judiciary_score

    # Predictability and Transparency of Policymaking / Data Quality
    if data_quality >= 8:
        transparency_score = "aa"
    elif data_quality >= 6:
        transparency_score = "a"
    else:
        transparency_score = "baa"
    scores['transparency'] = transparency_score

    # Agregação (pesos: 30% legislative, 30% judiciary, 40% transparency)
    leg_numeric = rating_to_numeric(legislative_score)
    jud_numeric = rating_to_numeric(judiciary_score)
    trans_numeric = rating_to_numeric(transparency_score)

    avg_numeric = leg_numeric * 0.30 + jud_numeric * 0.30 + trans_numeric * 0.40
    final_score = numeric_to_rating(avg_numeric)

    return final_score, scores

def calculate_fiscal_strength(
    primary_balance_gdp: float,
    debt_gdp: float,
    interest_burden: float,
    revenue_gdp: float
) -> Tuple[str, Dict]:
    """Calcula Fiscal Strength"""

    scores = {}

    # Fiscal Performance: Primary Balance
    if primary_balance_gdp > 5:
        perf_score = "aaa"
    elif primary_balance_gdp > 2:
        perf_score = "aa"
    elif primary_balance_gdp > 0:
        perf_score = "a"
    elif primary_balance_gdp > -3:
        perf_score = "baa"
    elif primary_balance_gdp > -6:
        perf_score = "ba"
    else:
        perf_score = "b"
    scores['performance'] = perf_score

    # Fiscal Burden: Debt and Interest
    if debt_gdp < 30:
        burden_score = "aaa"
    elif debt_gdp < 50:
        burden_score = "aa"
    elif debt_gdp < 70:
        burden_score = "a"
    elif debt_gdp < 90:
        burden_score = "baa"
    else:
        burden_score = "ba"
    scores['burden'] = burden_score

    # Fiscal Flexibility: Revenue
    if revenue_gdp > 25:
        flex_score = "aa"
    elif revenue_gdp > 20:
        flex_score = "a"
    else:
        flex_score = "baa"
    scores['flexibility'] = flex_score

    # Agregação (pesos: 40% performance, 40% burden, 20% flexibility)
    perf_numeric = rating_to_numeric(perf_score)
    burden_numeric = rating_to_numeric(burden_score)
    flex_numeric = rating_to_numeric(flex_score)

    avg_numeric = perf_numeric * 0.40 + burden_numeric * 0.40 + flex_numeric * 0.20
    final_score = numeric_to_rating(avg_numeric)

    return final_score, scores

def calculate_event_risk(
    external_vulnerability: str,  # low, moderate, high
    political_risk: str,
    banking_sector_risk: str,
    liquidity_risk: str
) -> Tuple[str, Dict]:
    """Calcula Susceptibility to Event Risk (usa função mínima)"""

    risk_levels = {"low": 0, "moderate": 1, "high": 2}

    risks = {
        "external_vulnerability": risk_levels.get(external_vulnerability, 0),
        "political_risk": risk_levels.get(political_risk, 0),
        "banking_sector_risk": risk_levels.get(banking_sector_risk, 0),
        "liquidity_risk": risk_levels.get(liquidity_risk, 0),
    }

    level = max(risks.values())

    if level == 0:
        return "Low", risks
    elif level == 1:
        return "Moderate", risks
    else:
        return "High", risks

# ============================================================
# Interface Streamlit
# ============================================================

st.title("📊 Moody's Sovereign Rating Methodology")
st.markdown("Simulador interativo da metodologia Moody's para ratings soberanos")

# Tabs principais
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Economic Strength",
    "Institutions & Governance",
    "Fiscal Strength",
    "Event Risk",
    "Results",
    "Summary",
    "Methodology"
])

# ============================================================
# TAB 1: Economic Strength
# ============================================================
with tab1:
    st.header("Economic Strength Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:
        gdp_growth = st.number_input(
            "Average Real GDP Growth (%)",
            value=2.5,
            step=0.1,
            help="Crescimento médio real do PIB em 10 anos"
        )

    with col2:
        mad_volatility = st.number_input(
            "MAD Volatility in Real GDP Growth (%)",
            value=0.8,
            step=0.1,
            help="Desvio Absoluto Mediano da volatilidade do PIB"
        )

    with col3:
        gdp_per_capita_ppp = st.number_input(
            "GDP per Capita (PPP, USD)",
            value=25000.0,
            step=1000.0,
            help="PIB per capita em paridade de poder de compra"
        )

    nominal_gdp = st.number_input(
        "Nominal GDP (US$ Billions)",
        value=1500.0,
        step=100.0,
        help="PIB nominal em bilhões USD"
    )

    # Calcular Economic Strength
    econ_score, econ_details = calculate_economic_strength(
        gdp_growth, mad_volatility, gdp_per_capita_ppp, nominal_gdp
    )

    st.divider()
    st.subheader("Sub-factor Scores")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Growth Dynamics", econ_details['growth'].upper())
    col2.metric("Volatility", econ_details['volatility'].upper())
    col3.metric("Scale of Economy", econ_details['scale'].upper())
    col4.metric("**Economic Strength**", econ_score.upper(), delta=None)

    st.session_state['econ_score'] = econ_score

# ============================================================
# TAB 2: Institutions & Governance
# ============================================================
with tab2:
    st.header("Institutions and Governance Strength Assessment")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Worldwide Governance Indicators (WGI)")
        wgi_govt_effectiveness = st.slider(
            "Government Effectiveness",
            min_value=-2.5,
            max_value=2.5,
            value=0.5,
            step=0.1,
            help="Range: -2.5 (weak) to 2.5 (strong)"
        )

        wgi_regulatory_quality = st.slider(
            "Regulatory Quality",
            min_value=-2.5,
            max_value=2.5,
            value=0.5,
            step=0.1,
            help="Range: -2.5 (weak) to 2.5 (strong)"
        )

        wgi_voice_accountability = st.slider(
            "Voice & Accountability",
            min_value=-2.5,
            max_value=2.5,
            value=0.3,
            step=0.1,
            help="Range: -2.5 (weak) to 2.5 (strong)"
        )

    with col2:
        st.subheader("Other Governance Factors")
        data_quality = st.slider(
            "Data Quality & Transparency (1-10)",
            min_value=1,
            max_value=10,
            value=7,
            help="Qualidade e transparência dos dados publicados"
        )

    # Calcular Institutions & Governance
    inst_score, inst_details = calculate_institutions_governance(
        wgi_govt_effectiveness, wgi_regulatory_quality, wgi_voice_accountability, data_quality
    )

    st.divider()
    st.subheader("Sub-factor Scores")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Legislative/Executive", inst_details['legislative'].upper())
    col2.metric("Judiciary", inst_details['judiciary'].upper())
    col3.metric("Transparency", inst_details['transparency'].upper())
    col4.metric("**Institutions**", inst_score.upper(), delta=None)

    st.session_state['inst_score'] = inst_score

# ============================================================
# TAB 3: Fiscal Strength
# ============================================================
with tab3:
    st.header("Fiscal Strength Assessment")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fiscal Performance")
        primary_balance = st.number_input(
            "Primary Balance (% of GDP)",
            value=0.5,
            step=0.1,
            help="Superávit/déficit primário em % do PIB"
        )

        debt_gdp = st.number_input(
            "General Government Debt (% of GDP)",
            value=65.0,
            step=1.0,
            help="Dívida bruta em % do PIB"
        )

    with col2:
        st.subheader("Fiscal Flexibility")
        interest_burden = st.number_input(
            "Interest Burden (% of revenues)",
            value=8.0,
            step=0.1,
            help="Despesa com juros em % das receitas"
        )

        revenue_gdp = st.number_input(
            "Government Revenue (% of GDP)",
            value=22.0,
            step=0.1,
            help="Receita do governo em % do PIB"
        )

    # Calcular Fiscal Strength
    fiscal_score, fiscal_details = calculate_fiscal_strength(
        primary_balance, debt_gdp, interest_burden, revenue_gdp
    )

    st.divider()
    st.subheader("Sub-factor Scores")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Performance", fiscal_details['performance'].upper())
    col2.metric("Burden", fiscal_details['burden'].upper())
    col3.metric("Flexibility", fiscal_details['flexibility'].upper())
    col4.metric("**Fiscal Strength**", fiscal_score.upper(), delta=None)

    st.session_state['fiscal_score'] = fiscal_score

# ============================================================
# TAB 4: Event Risk
# ============================================================
with tab4:
    st.header("Susceptibility to Event Risk")

    col1, col2 = st.columns(2)

    with col1:
        external_vuln = st.selectbox(
            "External Vulnerability Risk",
            ["Low", "Moderate", "High"],
            help="Risco de vulnerabilidade externa"
        )

        banking_risk = st.selectbox(
            "Banking Sector Risk",
            ["Low", "Moderate", "High"],
            help="Risco do setor bancário"
        )

    with col2:
        political_risk = st.selectbox(
            "Political Risk",
            ["Low", "Moderate", "High"],
            help="Risco político"
        )

        liquidity_risk = st.selectbox(
            "Government Liquidity Risk",
            ["Low", "Moderate", "High"],
            help="Risco de liquidez do governo"
        )

    event_risk, event_details = calculate_event_risk(
        external_vuln.lower(),
        political_risk.lower(),
        banking_risk.lower(),
        liquidity_risk.lower()
    )

    st.divider()
    st.subheader("Risk Assessment Details")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("External Vulnerability", external_vuln)
    col2.metric("Political Risk", political_risk)
    col3.metric("Banking Sector Risk", banking_risk)
    col4.metric("Liquidity Risk", liquidity_risk)

    st.divider()
    st.metric("Overall Event Risk", event_risk, delta=None)

    st.session_state['event_risk'] = event_risk

# ============================================================
# TAB 5: Results
# ============================================================
with tab5:
    st.header("Rating Results")

    # Recuperar scores calculados
    econ = st.session_state.get('econ_score', 'baa1')
    inst = st.session_state.get('inst_score', 'baa1')
    fiscal = st.session_state.get('fiscal_score', 'baa1')
    event = st.session_state.get('event_risk', 'Moderate')

    # Calcular Economic Resiliency (média de Economic + Institutions)
    econ_numeric = rating_to_numeric(econ)
    inst_numeric = rating_to_numeric(inst)
    economic_resiliency = numeric_to_rating((econ_numeric + inst_numeric) / 2)

    # Calcular Government Financial Strength (combinação ponderada)
    fiscal_numeric = rating_to_numeric(fiscal)
    # Pesos dinâmicos conforme a metodologia (exemplo: 60% resiliência, 40% fiscal)
    gfs_numeric = economic_resiliency_numeric = (econ_numeric + inst_numeric) / 2
    gfs = numeric_to_rating(gfs_numeric * 0.6 + fiscal_numeric * 0.4)

    # Calcular rating indicativo
    if event == "High":
        event_notch = -2
    elif event == "Moderate":
        event_notch = -1
    else:
        event_notch = 0

    gfs_numeric_final = rating_to_numeric(gfs)
    indicative_numeric = gfs_numeric_final + event_notch
    indicative_rating = numeric_to_rating(max(0, min(len(RATING_SCALE)-1, indicative_numeric)))

    # Display
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Economic Strength", econ.upper())
    col2.metric("Institutions", inst.upper())
    col3.metric("Fiscal Strength", fiscal.upper())
    col4.metric("Event Risk", event)

    st.divider()

    col1, col2 = st.columns(2)
    col1.metric("Economic Resiliency", economic_resiliency.upper())
    col2.metric("Government Financial Strength", gfs.upper())

    st.divider()

    st.metric("Scorecard-Indicated Rating", indicative_rating.upper(),
              help=f"Baseado em GFS ({gfs.upper()}) + Event Risk adjustment ({event_notch:+d})")

    # Radar chart
    st.subheader("Rating Profile Radar")

    factors = ['Economic', 'Institutional', 'Fiscal']
    values = [econ_numeric, inst_numeric, fiscal_numeric]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=factors,
        fill='toself',
        name='Scores',
        line=dict(color='#636EFA')
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 20])),
        showlegend=True,
        title="Rating Factor Profiles (lower is better)",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 6: Summary & Export
# ============================================================
with tab6:
    st.header("Summary & Export")

    # Recuperar todos os dados
    econ = st.session_state.get('econ_score', 'baa1')
    inst = st.session_state.get('inst_score', 'baa1')
    fiscal = st.session_state.get('fiscal_score', 'baa1')
    event = st.session_state.get('event_risk', 'Moderate')

    # Calcular ratings
    econ_numeric = rating_to_numeric(econ)
    inst_numeric = rating_to_numeric(inst)
    fiscal_numeric = rating_to_numeric(fiscal)

    economic_resiliency = numeric_to_rating((econ_numeric + inst_numeric) / 2)
    gfs_numeric = (econ_numeric + inst_numeric) / 2 * 0.6 + fiscal_numeric * 0.4
    gfs = numeric_to_rating(gfs_numeric)

    if event == "High":
        event_notch = -2
    elif event == "Moderate":
        event_notch = -1
    else:
        event_notch = 0

    indicative_numeric = rating_to_numeric(gfs) + event_notch
    indicative_rating = numeric_to_rating(max(0, min(len(RATING_SCALE)-1, indicative_numeric)))

    # Display Summary
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Rating Summary")
        summary_data = {
            "Factor": ["Economic Strength", "Institutions & Governance", "Fiscal Strength", "Event Risk"],
            "Score": [econ.upper(), inst.upper(), fiscal.upper(), event],
            "Status": ["✓", "✓", "✓", "✓"]
        }
        df_summary = pd.DataFrame(summary_data)
        st.dataframe(df_summary, use_container_width=True, hide_index=True)

    with col2:
        st.subheader("Derived Ratings")
        st.metric("Economic Resiliency", economic_resiliency.upper())
        st.metric("Gov't Financial Strength", gfs.upper())
        st.metric("**Final Rating**", indicative_rating.upper(), delta=f"{event_notch:+d} notch", delta_color="off")

    st.divider()

    # Export as JSON
    st.subheader("Export Analysis")

    export_data = {
        "Timestamp": pd.Timestamp.now().isoformat(),
        "Economic_Strength": econ,
        "Institutions_Governance": inst,
        "Fiscal_Strength": fiscal,
        "Event_Risk": event,
        "Economic_Resiliency": economic_resiliency,
        "Government_Financial_Strength": gfs,
        "Indicative_Rating": indicative_rating,
        "Event_Risk_Adjustment": event_notch
    }

    col1, col2 = st.columns(2)

    with col1:
        json_str = json.dumps(export_data, indent=2)
        st.download_button(
            label="📥 Download as JSON",
            data=json_str,
            file_name="moody_rating_analysis.json",
            mime="application/json"
        )

    with col2:
        csv_data = pd.DataFrame([export_data]).to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv_data,
            file_name="moody_rating_analysis.csv",
            mime="text/csv"
        )

    st.divider()

    # Comparison with other sovereigns (example)
    st.subheader("Comparison with Rating Categories")

    comparison_data = {
        "Rating": ["AAA", "AA", "A", "BAA", "BA", "B", "CAA"],
        "Category": ["Aaa/Aa1/Aa2/Aa3", "A1/A2/A3", "Baa1/Baa2/Baa3", "Ba1/Ba2/Ba3", "B1/B2/B3", "Caa1/Caa2/Caa3", "Ca/C"],
        "Meaning": [
            "Highest creditworthiness",
            "High creditworthiness",
            "Upper-medium creditworthiness",
            "Medium creditworthiness",
            "Speculative",
            "Highly speculative",
            "Minimal or in default"
        ]
    }

    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)

# ============================================================
# TAB 7: Methodology
# ============================================================
with tab7:
    st.header("Moody's Sovereign Rating Methodology")

    st.markdown("""
    ### Overview

    Moody's sovereign rating methodology evaluates credit risk of governments globally through a comprehensive scorecard approach.

    ### Key Components

    #### 1. **Economic Strength** (30%)
    - **Growth Dynamics**: Average real GDP growth (weighted 30%)
    - **Volatility**: Median absolute deviation of real GDP growth (weighted 35%)
    - **Scale of Economy**: GDP per capita in PPP terms (weighted 35%)

    #### 2. **Institutions and Governance Strength** (30%)
    - **Quality of Legislative/Executive Institutions** (30%): Based on WGI indicators
    - **Quality of Judiciary** (30%): Based on voice and accountability
    - **Data Quality & Transparency** (40%): Quality of economic and fiscal data

    #### 3. **Fiscal Strength** (40%)
    - **Fiscal Performance**: Primary balance as % of GDP
    - **Fiscal Burden**: Debt and interest metrics
    - **Fiscal Flexibility**: Revenue generation capacity

    #### 4. **Susceptibility to Event Risk**
    - **External Vulnerability Risk**
    - **Political Risk**
    - **Banking Sector Risk**
    - **Government Liquidity Risk**

    ### Rating Scale

    """)

    # Display rating scale
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Investment Grade:**")
        for i, rating in enumerate(RATING_SCALE[:13]):
            if i % 3 == 0:
                st.write(f"- {rating.upper()}")

    with col2:
        st.markdown("**Sub-Investment Grade:**")
        for rating in RATING_SCALE[13:19]:
            st.write(f"- {rating.upper()}")

    with col3:
        st.markdown("**Speculative:**")
        for rating in RATING_SCALE[19:]:
            st.write(f"- {rating.upper()}")

    st.divider()

    st.markdown("""
    ### Calculation Framework

    1. **Economic Resiliency** = Average of Economic Strength and Institutions/Governance
    2. **Government Financial Strength** = Weighted combination of Economic Resiliency (60%) and Fiscal Strength (40%)
    3. **Scorecard-Indicated Rating** = GFS adjusted for Event Risk

    ### Notes

    - The scorecard provides a range of three notches, not a precise rating
    - Analysts may apply judgment adjustments based on specific circumstances
    - This is a simplified simulation for educational purposes
    """)
