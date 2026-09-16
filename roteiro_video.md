# Roteiro do Video - Challenge Sprint 3

Tempo estimado: 4 a 5 minutos. Grave a tela no Colab rodando cada parte enquanto fala.


## 1) Abertura (30s)

"Ola, aqui e o grupo [nome do grupo]. Eu sou [seu nome], e comigo estao [outros nomes]. Esse video mostra a entrega do Challenge Sprint 3: probabilidade com distribuicao normal e regressao linear em Python."
"A base que usamos e a California Housing, com 20 mil registros de bairros da California. Tem renda mediana, idade dos imoveis, numero de quartos e o valor mediano do imovel, que e a variavel principal da analise."


## 2) Q1 - Probabilidade acima da mediana (1 min)

"Primeira questao: qual e a chance do valor de um imovel ficar acima da mediana? A gente calcula a mediana da coluna, padroniza ela na escala Z usando media e desvio da propria amostra, e pega a area da curva normal acima desse ponto."
"Deu aproximadamente 0,59. Ou seja, tem quase 60% de chance de um imovel sair acima da mediana. Como esperado, classificamos como provavel. Na base a media fica um pouco acima da mediana porque tem imoveis muito caros puxando o valor para cima."


## 3) Q2 - Intervalo de 2 desvios (1 min)

"Segunda questao: probabilidade de o valor cair dentro de media mais ou menos dois desvios-padrao. Para distribuicao normal isso bate a regra empirica dos 95 por cento."
"Os limites ficaram entre menos 0,24 e 4,38, e a probabilidade deu 0,9545. Classificacao: quase certo. Praticamente qualquer imovel cai nesse range."


## 4) Q3 - Regressao linear (1 min 30)

"Terceira questao: regressao linear entre renda mediana e valor do imovel. A ideia era ver se mais renda muda o preco."
"A reta ajustada deu: valor do imovel = 0,451 + 0,418 vezes a renda. Entao cada ponto a mais na renda mediana elevava em cerca de 0,42 o valor do imovel."
"O R2 ficou em 0,47 e a correlacao de Pearson em 0,69. Ou seja: renda sozinha explica menos da metade da variacao do preco. Tem outras variaveis na base que ajudam, tipo idade do imovel ou localizacao, mas aqui a regressao simples ja bota bem qual e a relacao geral."


## 5) Encerramento (30s)

"E isso, entao a gente resolveu: probabilidade acima da mediana classificada como provavel, o intervalo de dois desvios classificado como quase certo, e a regressao linear com coeficiente positivo e R2 de 0,47. O codigo, os graficos e a base estao no repositorio do GitHub que a gente mandou no texto."
