# 📖 Guia de Referência - Inputs do App Moody's

## Economic Strength Inputs

### Average Real GDP Growth (%)
- **O que é**: Crescimento médio do PIB real em termos anuais (últimos ~10 anos)
- **Onde encontrar**: FMI World Economic Outlook, Banco Mundial
- **Interpretação**:
  - > 4.5% = AAA (Crescimento muito forte)
  - 3.0-4.5% = AA (Crescimento forte)
  - 2.0-3.0% = A (Crescimento moderado)
  - 0-2.0% = BAA (Crescimento fraco)
  - < 0% = BA ou inferior (Estagnação/recessão)
- **Exemplos**: 
  - Índia: 6.5%
  - China: 4.8%
  - EUA: 2.8%
  - Japão: 1.3%

### MAD Volatility in Real GDP Growth (%)
- **O que é**: Desvio Absoluto Mediano da volatilidade do crescimento do PIB
- **Onde encontrar**: Cálculos a partir de série histórica do PIB
- **Interpretação**:
  - < 0.3% = AAA (Crescimento muito estável)
  - 0.3-0.9% = AA-A (Crescimento estável)
  - 0.9-1.5% = BAA (Crescimento com volatilidade moderada)
  - > 1.5% = BA ou inferior (Crescimento muito volátil)
- **Exemplos**:
  - Suíça: 0.6% (Muito estável)
  - Brasil: 1.8% (Volátil)
  - Argentina: 2.5% (Muito volátil)

### GDP per Capita (PPP, USD)
- **O que é**: PIB per capita em paridade de poder de compra em dólares americanos
- **Onde encontrar**: FMI, Banco Mundial, OCDE
- **Interpretação**: Mede o nível de desenvolvimento e renda per capita
- **Exemplos**:
  - Luxemburgo: $138,000
  - EUA: $76,000
  - Brasil: $15,000
  - Índia: $6,800

### Nominal GDP (US$ Billions)
- **O que é**: Tamanho total da economia em dólares americanos
- **Onde encontrar**: FMI, Banco Mundial, Banco Central
- **Interpretação**: Maior PIB = maior capacidade de gerar receita
- **Exemplos**:
  - EUA: $27,360 bilhões
  - China: $17,920 bilhões
  - Japão: $4,230 bilhões
  - Brasil: $1,839 bilhões

---

## Institutions & Governance Inputs

### Government Effectiveness (WGI)
- **O que é**: Indicador do Banco Mundial sobre a qualidade e previsibilidade da política pública
- **Range**: -2.5 (fraco) a +2.5 (forte)
- **Onde encontrar**: World Bank Worldwide Governance Indicators
- **Interpretação**:
  - > 1.5 = AAA (Governo altamente eficaz)
  - 1.0-1.5 = AA (Governo eficaz)
  - 0.5-1.0 = A (Governo razoavelmente eficaz)
  - 0-0.5 = BAA (Governo moderadamente eficaz)
  - < 0 = BA ou inferior (Governo ineficaz)

### Regulatory Quality (WGI)
- **O que é**: Capacidade do governo de formular e implementar políticas regulatórias efetivas
- **Range**: -2.5 (fraco) a +2.5 (forte)
- **Onde encontrar**: World Bank Worldwide Governance Indicators
- **Interpretação**: Similar ao Government Effectiveness

### Voice & Accountability (WGI)
- **O que é**: Grau de liberdade de expressão, liberdade de imprensa e democracia
- **Range**: -2.5 (fraco) a +2.5 (forte)
- **Onde encontrar**: World Bank Worldwide Governance Indicators

### Data Quality & Transparency (1-10)
- **O que é**: Qualidade, oportunidade e confiabilidade dos dados econômicos e fiscais publicados
- **Como avaliar**:
  - 9-10: Dados publicados regularmente, revisões pequenas, sem atrasos
  - 7-8: Dados publicados com pequenos atrasos, algumas revisões
  - 5-6: Dados com atrasos ou revisões significativas
  - 3-4: Dados incompletos ou com inconsistências
  - 1-2: Dados confiáveis questionáveis ou ausentes

---

## Fiscal Strength Inputs

### Primary Balance (% of GDP)
- **O que é**: Resultado primário (receita - despesa corrente) em % do PIB
- **Onde encontrar**: Banco Central, Tesouro
- **Interpretação**:
  - > 5% = AAA (Superávit forte)
  - 2-5% = AA (Superávit moderado)
  - 0-2% = A (Equilibrado/pequeno superávit)
  - -3 a 0% = BAA (Pequeno a moderado déficit)
  - -6 a -3% = BA (Déficit significativo)
  - < -6% = B ou inferior (Déficit muito alto)

### General Government Debt (% of GDP)
- **O que é**: Total da dívida bruta do governo em % do PIB
- **Onde encontrar**: Banco Central, Tesouro
- **Interpretação**:
  - < 30% = AAA (Dívida muito baixa)
  - 30-50% = AA (Dívida baixa)
  - 50-70% = A (Dívida moderada)
  - 70-90% = BAA (Dívida alta)
  - > 90% = BA ou inferior (Dívida muito alta)
- **Exemplos**:
  - Luxemburgo: 25%
  - Alemanha: 66%
  - Brasil: 70%
  - Japão: 264% (caso especial: dívida em moeda doméstica)

### Interest Burden (% of revenues)
- **O que é**: Despesa com juros em % das receitas do governo
- **Onde encontrar**: Banco Central, Tesouro
- **Interpretação**: Indica a sustentabilidade fiscal
- **Exemplos**:
  - Alemanha: 5.2%
  - Brasil: 18.5%
  - Turquia: 25%

### Government Revenue (% of GDP)
- **O que é**: Receita do governo (impostos + outras receitas) em % do PIB
- **Onde encontrar**: Banco Central, Tesouro
- **Interpretação**: Maior receita = mais flexibilidade fiscal
- **Exemplos**:
  - Suécia: 42%
  - Alemanha: 39%
  - EUA: 27%
  - Índia: 18%

---

## Event Risk Inputs

### External Vulnerability Risk
- **Low**: Posição de conta corrente saudável, reservas adequadas
- **Moderate**: Algumas vulnerabilidades externas
- **High**: Déficit em conta corrente grande, baixas reservas, dívida externa alta

### Political Risk
- **Low**: Instituições políticas estáveis, democracia consolidada
- **Moderate**: Alguma instabilidade política ou incerteza
- **High**: Conflito político, instabilidade institucional, risco de golpe

### Banking Sector Risk
- **Low**: Setor bancário saudável, boa capitalização
- **Moderate**: Alguns problemas no setor bancário
- **High**: Crise bancária, insolvência de grandes bancos

### Government Liquidity Risk
- **Low**: Acesso fácil aos mercados de capital, reservas adequadas
- **Moderate**: Alguns problemas de refinanciamento
- **High**: Dificuldade em refinanciar a dívida, risco de default

---

## 🔗 Fontes Recomendadas de Dados

1. **FMI (IMF)**: World Economic Outlook, International Financial Statistics
2. **Banco Mundial**: World Bank Open Data, Governance Indicators
3. **OCDE**: Statistics Database
4. **Bancos Centrais**: Estatísticas oficiais
5. **Reuters/Bloomberg**: Dados de mercado
6. **S&P Global, Moody's**: Publicações oficiais

---

## 💡 Dicas de Uso

- **Consistência**: Use dados do mesmo período (ex: sempre do mesmo ano fiscal)
- **Confiabilidade**: Prefira fontes oficiais em vez de estimativas
- **Comparações**: Compare com países similares para avaliar relatividade
- **Tendências**: Observe variações ao longo do tempo, não apenas um ponto em tempo
- **Ajustes**: Considere fatores especiais (crises, reformas, descobertas)

---

## 📊 Exemplo de Análise

### País: Brasil

**Economic Strength**
- GDP Growth: 2.2%
- MAD Volatility: 1.8%
- GDP per Capita PPP: $15,000
- Resultado: BAA (Moderado)

**Institutions & Governance**
- Government Effectiveness: 0.1 (Moderado)
- Regulatory Quality: 0.2 (Moderado)
- Voice & Accountability: 0.5 (Moderado)
- Data Quality: 6/10 (Moderada)
- Resultado: BAA (Moderado)

**Fiscal Strength**
- Primary Balance: -1.5%
- Debt: 70%
- Interest Burden: 18.5%
- Revenue: 31%
- Resultado: BA (Abaixo de moderado)

**Event Risk**: Moderate (-1 notch)

**Rating Indicativo Final**: BB+ (Especulativo)
