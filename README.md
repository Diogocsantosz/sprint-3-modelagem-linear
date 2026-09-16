# Challenge Sprint 3 - Probabilidade e Regressão Linear

Trabalho de estatística usando a base **California Housing** (20.640 registros). Tudo foi feito em Python e roda direto no Google Colab.

## O que tem aqui

- `california_housing.csv` — a base de dados usada nas análises
- `gerar_dados.py` — script que baixa a base do scikit-learn e salva o CSV
- `challenge_sprint3.py` — o mesmo código do notebook, em formato de script
- `challenge_sprint3.ipynb` — notebook com o código e os resultados (abre no Colab)
- `q1_acima_mediana.png`, `q2_intervalo.png`, `q3_regressao.png` — gráficos gerados

## O que foi resolvido

**Q1 — Probabilidade acima da mediana.** Assumindo distribuição normal para o valor mediano dos imóveis, calculamos Z = (mediana − média) / desvio e achamos P(X > mediana) ≈ 0,59. Evento classificado como **provável**.

**Q2 — Probabilidade no intervalo média ± 2 desvios.** O intervalo ficou em [−0,24; 4,38] e a probabilidade em ≈ 0,9545 — praticamente a regra empírica dos 95%. Evento **quase certo**.

**Q3 — Regressão linear.** Modelo: valor do imóvel = 0,451 + 0,418 × renda mediana. R² = 0,47 e correlação de Pearson = 0,69. Ou seja: renda mediana sobe, preço sobe junto, mas a renda sozinha explica menos da metade da variação do preço.

