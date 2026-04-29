# Moody's Sovereign Rating Methodology - Streamlit App

Um simulador interativo da metodologia de ratings soberanos da Moody's implementado em Streamlit.

## 📊 Visão Geral

Este aplicativo implementa a metodologia de avaliação de crédito de soberanos da Moody's, permitindo que você:

- Avalie a **força econômica** de um país
- Analise a **qualidade institucional e de governança**
- Calcule a **força fiscal** do governo
- Avalie a **suscetibilidade a riscos de eventos**
- Obtenha um **rating de crédito indicativo**

## 🚀 Como Usar

### 1. Instalação de Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a Aplicação

```bash
streamlit run moody_app.py
```

O app será aberto automaticamente no seu navegador em `http://localhost:8501`

## 📋 Abas Principais

### 1. **Economic Strength** (Força Econômica)
Avalia o desempenho econômico do país através de:
- **Crescimento Real do PIB**: Média de crescimento real (últimos 10 anos)
- **Volatilidade do PIB**: Desvio Absoluto Mediano (MAD)
- **Escala da Economia**: PIB per capita em paridade de poder de compra

### 2. **Institutions & Governance** (Instituições e Governança)
Mede a qualidade institucional através de:
- **Efetividade do Governo**: Indicador WGI de efetividade governamental
- **Qualidade Regulatória**: Capacidade de formular e implementar políticas
- **Voz e Accountability**: Liberdade de expressão e participação política
- **Qualidade de Dados**: Transparência e confiabilidade dos dados

### 3. **Fiscal Strength** (Força Fiscal)
Analisa a sustentabilidade fiscal através de:
- **Performance Fiscal**: Balanço primário como % do PIB
- **Carga de Dívida**: Dívida bruta e despesa com juros
- **Flexibilidade Fiscal**: Capacidade de gerar receitas

### 4. **Event Risk** (Risco de Eventos)
Avalia fatores de risco de curto prazo:
- **Risco de Vulnerabilidade Externa**: Posição de conta corrente e externos
- **Risco Político**: Estabilidade e previsibilidade política
- **Risco do Setor Bancário**: Saúde do setor financeiro
- **Risco de Liquidez**: Capacidade de financiamento do governo

### 5. **Results** (Resultados)
Exibe:
- Scores de todos os fatores
- Rating de resiliência econômica
- Força financeira do governo
- Rating indicativo final
- Gráfico radar com o perfil de ratings

### 6. **Summary** (Resumo)
Permite:
- Visualizar um resumo completo da análise
- Exportar resultados em JSON ou CSV
- Comparar com categorias de ratings internacionais

### 7. **Methodology** (Metodologia)
Explicação detalhada da metodologia Moody's

## 📐 Metodologia de Cálculo

### Economic Resiliency
```
Economic Resiliency = (Economic Strength + Institutions & Governance) / 2
```

### Government Financial Strength (GFS)
```
GFS = (Economic Resiliency × 0.60) + (Fiscal Strength × 0.40)
```

### Scorecard-Indicated Rating
```
Indicative Rating = GFS + Event Risk Adjustment
```

**Event Risk Adjustment:**
- High Event Risk: -2 notches
- Moderate Event Risk: -1 notch
- Low Event Risk: 0 notches

## 📊 Escala de Ratings

### Investment Grade
- **AAA**: Creditabilidade máxima
- **AA**: Creditabilidade muito alta
- **A**: Creditabilidade alta
- **BAA**: Creditabilidade média

### Speculative Grade
- **BA**: Especulativo
- **B**: Altamente especulativo
- **CAA/CA/C**: Risco mínimo ou inadimplência

## 💾 Exportação de Dados

Os resultados podem ser exportados em dois formatos:

1. **JSON**: Para integração com sistemas
2. **CSV**: Para análise em planilhas

## 🔧 Funcionalidades

✅ Interface intuitiva com abas separadas  
✅ Cálculos automáticos de ratings  
✅ Gráficos interativos (Radar Chart)  
✅ Exportação de resultados  
✅ Comparação com padrões internacionais  
✅ Metodologia baseada na Moody's 2022  

## 📖 Referências

- Moody's Investors Service - Sovereign and Supranational Rating Methodology (22 de novembro de 2022)
- Worldwide Governance Indicators (WGI)

## ⚙️ Requisitos do Sistema

- Python 3.8+
- pip ou conda

## 📝 Notas Importantes

- Este é um simulador educacional baseado na metodologia Moody's
- As thresholds e pesos foram simplificados para fins didáticos
- Resultados reais podem variar em relação aos ratings oficiais da Moody's
- Para análises comerciais, consulte relatórios oficiais da Moody's

## 🤝 Suporte

Para dúvidas ou sugestões, consulte a documentação oficial da Moody's Investors Service.

---

**Versão**: 1.0  
**Data**: 2024  
**Baseado em**: Moody's Sovereign Rating Methodology (Nov 2022)
