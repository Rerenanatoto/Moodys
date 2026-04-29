# 📋 Projeto Completo: Moody's Sovereign Rating Methodology em Streamlit

## 📦 Arquivos Inclusos

### 1. **moody_app.py** (Principal)
Aplicação Streamlit completa com:
- 7 abas interativas
- Cálculos automáticos de ratings
- Exportação de dados
- Gráficos interativos
- Interface responsiva

### 2. **README.md**
Documentação principal com:
- Instruções de instalação e uso
- Descrição das 7 abas
- Metodologia de cálculo
- Escala de ratings
- Funcionalidades

### 3. **REFERENCE_GUIDE.md**
Guia detalhado de inputs com:
- O que é cada indicador
- Onde encontrar dados
- Interpretação dos valores
- Exemplos por país
- Dicas de uso

### 4. **example_countries.json**
Dados de exemplo para 8 países:
- Estados Unidos
- Alemanha
- Japão
- Brasil
- Índia
- México
- Turquia
- Argentina

### 5. **requirements.txt**
Dependências do projeto:
- streamlit
- pandas
- numpy
- plotly

---

## 🚀 Quick Start

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar o app
streamlit run moody_app.py

# 3. Abrir no navegador
# http://localhost:8501
```

---

## 📊 Estrutura da Aplicação

```
moody_app.py
├── Configuração
│   ├── Page config
│   ├── Constantes
│   └── Session state
│
├── Funções Auxiliares
│   ├── Rating conversion
│   ├── WGI classification
│   └── Export functions
│
├── Funções de Cálculo
│   ├── calculate_economic_strength()
│   ├── calculate_institutions_governance()
│   ├── calculate_fiscal_strength()
│   └── calculate_event_risk()
│
└── Interface (Streamlit)
    ├── Tab 1: Economic Strength
    ├── Tab 2: Institutions & Governance
    ├── Tab 3: Fiscal Strength
    ├── Tab 4: Event Risk
    ├── Tab 5: Results
    ├── Tab 6: Summary & Export
    └── Tab 7: Methodology
```

---

## 📐 Metodologia Implementada

### Economic Strength (30%)
```python
def calculate_economic_strength(gdp_growth, mad_volatility, gdp_per_capita_ppp, nominal_gdp):
    # Thresholds para cada métrica
    # Pesos: 30% crescimento, 35% volatilidade, 35% escala
    # Resultado: AAA a CAA
```

### Institutions & Governance (30%)
```python
def calculate_institutions_governance(wgi_effectiveness, wgi_regulatory, wgi_voice, data_quality):
    # WGI score classification
    # Data quality evaluation
    # Pesos: 30% legislativo, 30% judiciário, 40% transparência
    # Resultado: AAA a CA
```

### Fiscal Strength (40%)
```python
def calculate_fiscal_strength(primary_balance, debt, interest_burden, revenue):
    # Performance: primary balance thresholds
    # Burden: debt level classification
    # Flexibility: revenue capacity
    # Pesos: 40% performance, 40% burden, 20% flexibility
    # Resultado: AAA a B
```

### Event Risk Assessment
```python
def calculate_event_risk(external_vuln, political_risk, banking_risk, liquidity_risk):
    # Função mínima: o nível mais alto de risco prevalece
    # Low: 0 notches, Moderate: -1 notch, High: -2 notches
```

### Final Rating Calculation
```python
Economic Resiliency = (Economic Strength + Institutions) / 2
Gov't Financial Strength = (Economic Resiliency × 0.6) + (Fiscal Strength × 0.4)
Final Rating = GFS + Event Risk Adjustment
```

---

## 🎨 Features da Interface

### ✅ Validação de Inputs
- Ranges automáticos para cada campo
- Valores padrão realistas
- Unidades claramente indicadas

### ✅ Cálculos em Tempo Real
- Session state para persistência
- Auto-atualização de métricas
- Conversão automática de scales

### ✅ Visualizações
- Radar chart dos 5 fatores
- Métricas com deltas
- Dataframes interativos

### ✅ Exportação
- JSON: Para integração
- CSV: Para análise
- Timestamp automático

### ✅ Documentação
- Tooltips em cada input
- Explicações detalhadas
- Exemplos de países

---

## 📈 Exemplos de Uso

### Exemplo 1: Análise de País Desenvolvido (Alemanha)

**Inputs:**
- GDP Growth: 1.9%
- MAD Volatility: 0.9%
- GDP per Capita: $62,050
- WGI Govt Effectiveness: 1.9
- WGI Regulatory Quality: 1.6
- Primary Balance: 2.5%
- Debt: 66%
- Revenue: 39%

**Output:**
- Economic Strength: AA
- Institutions: AA
- Fiscal Strength: AA
- Economic Resiliency: AA
- Gov't Financial Strength: AA
- **Final Rating: AAA**

### Exemplo 2: Análise de País em Desenvolvimento (Brasil)

**Inputs:**
- GDP Growth: 2.2%
- MAD Volatility: 1.8%
- GDP per Capita: $15,000
- WGI Govt Effectiveness: 0.1
- WGI Regulatory Quality: 0.2
- Primary Balance: -1.5%
- Debt: 70%
- Revenue: 31%
- Event Risk: Moderate

**Output:**
- Economic Strength: BAA
- Institutions: BAA
- Fiscal Strength: BA
- Economic Resiliency: BAA
- Gov't Financial Strength: BAA
- **Final Rating: BB+**

---

## 🔧 Customizações Possíveis

### 1. Adicionar Mais Indicadores
```python
# No dicionário RATING_SCALE ou nas funções de cálculo
EXTERNAL_DEBT_RATIOS = {...}
RESERVE_ADEQUACY = {...}
```

### 2. Mudar Pesos
```python
# Ajustar pesos dinâmicos por classe de país
if gdp_per_capita < 5000:
    # Pesos diferentes para países menos desenvolvidos
```

### 3. Integrar com Database
```python
# Conectar a uma base de dados de indicadores
# Carregar dados reais automaticamente
```

### 4. Adicionar Comparações
```python
# Comparar país com peers ou benchmarks
# Mostrar histórico de ratings
```

---

## 🎓 Fontes Metodológicas

- **Moody's Investors Service**: Sovereign Rating Methodology (Nov 2022)
- **World Bank**: Worldwide Governance Indicators
- **IMF**: World Economic Outlook
- **OCDE**: Statistical Databases

---

## 📞 Suporte e Contribuições

Este é um projeto educacional simulando a metodologia Moody's.

**Limitações:**
- Versão simplificada para fins didáticos
- Ratings reais podem variar
- Thresholds adaptados para demonstração
- Não substitui análises profissionais

**Para análises comerciais**, consulte:
- Relatórios oficiais da Moody's
- Consultores especializados em credit rating
- Documentação técnica completa da Moody's

---

## 📝 Licença

Este projeto foi criado como simulador educacional da metodologia Moody's.

---

**Versão**: 1.0  
**Data de Criação**: 2024  
**Atualização**: 2024  
**Baseado em**: Moody's Sovereign Rating Methodology (22 de novembro de 2022)
