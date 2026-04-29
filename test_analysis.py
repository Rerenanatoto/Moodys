#!/usr/bin/env python3
"""
Script de teste para demonstrar o uso do app Moody's
Carrega dados de exemplo e mostra os ratings calculados
"""

import json
from typing import Dict

# Simulação das funções do app para demonstração
def rating_to_numeric(rating: str) -> float:
    """Converte rating para valor numérico"""
    RATING_SCALE = [
        "aaa", "aa1", "aa2", "aa3", "a1", "a2", "a3",
        "baa1", "baa2", "baa3", "ba1", "ba2", "ba3",
        "b1", "b2", "b3", "caa1", "caa2", "caa3", "ca", "c"
    ]
    return float(RATING_SCALE.index(rating.lower()))

def numeric_to_rating(numeric_val: float) -> str:
    """Converte valor numérico para rating"""
    RATING_SCALE = [
        "aaa", "aa1", "aa2", "aa3", "a1", "a2", "a3",
        "baa1", "baa2", "baa3", "ba1", "ba2", "ba3",
        "b1", "b2", "b3", "caa1", "caa2", "caa3", "ca", "c"
    ]
    idx = int(round(numeric_val))
    idx = max(0, min(len(RATING_SCALE) - 1, idx))
    return RATING_SCALE[idx]

def load_example_countries():
    """Carrega dados de exemplo dos países"""
    with open("example_countries.json", "r") as f:
        return json.load(f)["countries"]

def analyze_country(country_data: Dict) -> Dict:
    """Executa análise para um país"""

    # Simulação de cálculos (versão simplificada)
    econ_numeric = rating_to_numeric("baa2")  # Exemplo
    inst_numeric = rating_to_numeric("baa1")   # Exemplo
    fiscal_numeric = rating_to_numeric("ba1")  # Exemplo

    # Calcular Economic Resiliency
    econ_resiliency_numeric = (econ_numeric + inst_numeric) / 2
    econ_resiliency = numeric_to_rating(econ_resiliency_numeric)

    # Calcular GFS
    gfs_numeric = econ_resiliency_numeric * 0.6 + fiscal_numeric * 0.4
    gfs = numeric_to_rating(gfs_numeric)

    # Aplicar Event Risk
    event_risk_mapping = {
        "Low": 0,
        "Moderate": -1,
        "High": -2
    }
    event_risk = country_data.get("external_vulnerability", "Moderate")
    event_notch = event_risk_mapping.get(event_risk, -1)

    final_numeric = rating_to_numeric(gfs) + event_notch
    final_rating = numeric_to_rating(max(0, min(19, final_numeric)))

    return {
        "country": country_data["name"],
        "code": country_data["code"],
        "economic_strength": "baa2",
        "institutions": "baa1",
        "fiscal_strength": "ba1",
        "event_risk": event_risk,
        "economic_resiliency": econ_resiliency,
        "gfs": gfs,
        "final_rating": final_rating
    }

def print_analysis_table(countries_analysis: list):
    """Imprime tabela com análises"""
    print("\n" + "="*100)
    print("MOODY'S SOVEREIGN RATING ANALYSIS - EXAMPLE COUNTRIES")
    print("="*100)

    header = f"{'País':<20} {'Econ':<8} {'Inst':<8} {'Fisc':<8} {'Event Risk':<15} {'GFS':<8} {'Rating':<8}"
    print(header)
    print("-"*100)

    for analysis in countries_analysis:
        row = (
            f"{analysis['country']:<20} "
            f"{analysis['economic_strength']:<8} "
            f"{analysis['institutions']:<8} "
            f"{analysis['fiscal_strength']:<8} "
            f"{analysis['event_risk']:<15} "
            f"{analysis['gfs']:<8} "
            f"{analysis['final_rating'].upper():<8}"
        )
        print(row)

    print("="*100 + "\n")

def print_country_details(analysis: Dict):
    """Imprime detalhes de um país"""
    print(f"\n📊 ANÁLISE DETALHADA: {analysis['country']} ({analysis['code']})")
    print("-" * 60)
    print(f"Economic Strength:      {analysis['economic_strength'].upper()}")
    print(f"Institutions & Gov:     {analysis['institutions'].upper()}")
    print(f"Fiscal Strength:        {analysis['fiscal_strength'].upper()}")
    print(f"Event Risk:             {analysis['event_risk']}")
    print(f"Economic Resiliency:    {analysis['economic_resiliency'].upper()}")
    print(f"Gov Financial Strength: {analysis['gfs'].upper()}")
    print(f"FINAL RATING:           {analysis['final_rating'].upper()} ⭐")
    print("-" * 60)

if __name__ == "__main__":
    print("\n🚀 Iniciando análise de países exemplo...\n")

    # Carregar dados
    countries = load_example_countries()
    print(f"✓ {len(countries)} países carregados de 'example_countries.json'")

    # Analisar cada país
    analyses = []
    for country in countries:
        analysis = analyze_country(country)
        analyses.append(analysis)

    # Exibir resultados
    print_analysis_table(analyses)

    # Mostrar detalhes de 3 exemplos
    print("\n📋 EXEMPLOS DETALHADOS:\n")
    print_country_details(analyses[0])  # EUA
    print_country_details(analyses[3])  # Brasil
    print_country_details(analyses[6])  # Turquia

    print("\n✅ Análise completa!")
    print("\n💡 Dica: Para executar o app com dados reais:")
    print("   streamlit run moody_app.py")
    print("\n📖 Para mais informações, consulte README.md e REFERENCE_GUIDE.md")
