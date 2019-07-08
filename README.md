# My Machine Learning Journey

## What is it?
This repository consists of the materials used and developed during my studies on machine learning. Small scale machine learning projects to understand the core concepts

### Who am I
My name is Clarissa Lima, I am a graduate student in Information Systems at UFMG and a graduate student in Control and Automation Engineering at PUC-Minas. Look at my profile later to know more about me :)

<!--### What to study?
Things you need to study before start sudying Machine Learning:
 * [Iniciante](#árvore-de-decisão)
 * [KNN](#KNN)
 * [Naive bayes](#naive-bayes)-->

![Screenshot](img.png)

## Table of contents
* [Why study Machine Learning](#why-study-machine-learning)
* [Material](#material)

## Why study Machine Learning

(*** need to complete this part ***)


## Material
  - [Linear Regression](#linear-regression)
  - [SVM](#svm)
  - [KNN](#knn)
  - [Regressão Logística](#regressao-logistica)
  - [Decision Tree](#decision-tree)
  - [K-Means](#k-means)
  - [Floresta aleatória](#floresta-aleatoria)
  - [Baías ingénuas](#baias-ingenuas)
  - [Algoritmos de redução dimensional](#algoritmos-de-reducao-dimensional)
  - [Algoritmos de aumento de gradiente](#algoritmos-de-aumento-de-gradiente)
  - [Métodos do Ensemble](#metodos-do-ensemble)
  - [Agregacao de Algoritmos](#agregacao-de-algoritmos)
  - [Análise de Componentes Principais](#analise-de-componentes-principais)
  - [Decomposição de valores singulares](#decomposicao-de-valores-singulares)
  - [Análise de Componentes Independentes](analise-de-componentes-independentes)



Algumas das aplicações do ACP incluem compressão, simplificando dados para facilitar a aprendizagem, a visualização. Observe que o conhecimento do domínio é muito importante ao escolher se deseja prosseguir com o ACP ou não. Não é adequado nos casos em que os dados são ruidosos (todos os componentes do ACP têm uma variação bastante alta).
  
  
<!-- * [Árvore de decisão](#árvore-de-decisão)
 * [KNN](#KNN)
 * [Naive bayes](#naive-bayes)
 * [Support vector machine(SVM)](#support-vector-machine(SVM))
 * [Regressão linear](#regressão-linear)
 * [Perceptron](#perceptron)
 * [Regressão logística](#regressao-logistica)
 * [Função de custo](##função-de-custo)
 * [Gradient Descent](#gradient-Descent)
 * [Multilayer perceptron](#multilayer-perceptron)
 * [Redes neurais convolucionais](#redes-neurais-convolucionais)
 * [Rede neurais recorrentes](#rede-neurais-recorrentes)
 * [Machine learning não superviosionado](#machine-learning-não-superviosionado)
# Árvore de decisão
(*** need to complete this part ***)
# KNN
(*** need to complete this part ***)
# Naive bayes
(*** need to complete this part ***)
# Support vector machine(SVM)
(*** need to complete this part ***)
# Regressão linear
(*** need to complete this part ***)
# Perceptron
(*** need to complete this part ***)
# Regressão logística
(*** need to complete this part ***)
# Função de custo
(*** need to complete this part ***)
# Gradient Descent
(*** need to complete this part ***)
# Multilayer perceptron
(*** need to complete this part ***)
# Rede neurais recorrentes
(*** need to complete this part ***)
# Machine learning não superviosionado
(*** need to complete this part ***)
-->


```
$ cd ../lorem
$ npm install
$ npm start
```

# Regressão linear
O algoritmo de Regressão linear usará os pontos de dados para encontrar a melhor linha de ajuste para modelar os dados. Uma linha pode ser representada pela equação, y = m * x + c onde y é a variável dependente e xé a variável independente. As teorias básicas de cálculo são aplicadas para encontrar os valores para m e c usando o conjunto de dados fornecido.
A Regressão linear tem 2 tipos como Regressão linear simples, onde são utilizadas apenas 1 variável independente e Regressão linear múltipla, onde múltiplas variáveis ​​independentes são definidas.

### Regime de mínimos quadrados comuns:
se você conhece estatísticas, provavelmente já ouviu falar de regressão linear antes. Os mínimos quadrados são um método para realizar a regressão linear. Você pode pensar em regressão linear como a tarefa de ajustar uma linha reta através de um conjunto de pontos. Existem várias estratégias possíveis para fazer isso, e a estratégia “mínimos quadrados comuns” é assim: você pode desenhar uma linha e, em seguida, para cada um dos pontos de dados, medir a distância vertical entre o ponto e a linha, e adicioná-los ; a linha ajustada seria aquela em que essa soma de distâncias seja tão pequena quanto possível.



Linear refere-se ao tipo de modelo que você está usando para ajustar os dados, enquanto os mínimos quadrados se referem ao tipo de métrica de erro em que você está minimizando.

# SVM
Isso pertence ao algoritmo do tipo de classificação. O algoritmo irá separar os pontos de dados usando uma linha. Esta linha é escolhida de tal forma que será mais importante dos pontos de dados mais próximos em 2 categorias.
O SMV é um algoritmo de classificação binária. Dado um conjunto de pontos de 2 tipos no lugar N dimensional, SMV gera um hiperlane dimensional (N-1) para separar esses pontos em 2 grupos. Digamos que você tenha alguns pontos de 2 tipos em um papel que são linearmente separáveis. O SMV encontrará uma linha recta que separa esses pontos em 2 tipos e está localizada o mais longe possível de todos esses pontos.

Em termos de escala, alguns dos maiores problemas que foram resolvidos usando SMVs (com implementações adequadamente modificadas) são exibições publicitárias, reconhecimento de site de splice humano, detecção de gênero baseada em imagem, classificação de imagem em larga escala…


# KNN 
Este é um algoritmo simples que prevê pontos de dados desconhecidos com os seus vizinhos mais próximos. O valor de k é um fator crítico aqui quanto à precisão da predição. Ele determina o mais próximo ao calcular a distância usando funções básicas de distância como Euclidean. No entanto, esse algoritmo precisa de alto poder de computação e precisamos normalizar os dados inicialmente para trazer todos os pontos de dados para o mesmo intervalo.

# Regressao Logistica
A regressão logística é usada onde uma saída discreta é esperada, como a ocorrência de algum evento (ex. Prever se a chuva irá ocorrer ou não).Normalmente, a regressão logística usa alguma função para espremer valores para um determinado intervalo.
“Sigmoid” (função logística) é uma das funções que possui a curva de forma “S” utilizada para a classificação binária. Converte valores para o intervalo de 0, 1 que interpretou como uma probabilidade de ocorrer algum evento.
y = e ^ (b0 + b1 * x) / (1 + e ^ (b0 + b1 * x))
Acima é uma equação de regressão logística simples onde b0, b1 são constantes. Enquanto os valores de treinamento para estes serão calculados de tal forma que o erro entre a predição eo valor real se torne mínimo.
A regressão logística é uma poderosa maneira estatística de modelar um resultado binomial com uma ou mais variáveis explicativas. Ele mede a relação entre a variável categórica dependente e uma ou mais variáveis independentes estimando probabilidades usando uma função logística, que é a distribuição logística cumulativa.



Em geral, as regressões podem ser usadas em aplicações do mundo real, tais como:
– Pontuação de crédito
– Medindo as taxas de sucesso das campanhas de marketing
– Previsão das receitas de um determinado produto
– Haverá um terremoto em um determinado dia?

# Decision Tree
Este algoritmo classifica a população para vários conjuntos com base em algumas propriedades escolhidas (variáveis independentes) de uma população. Geralmente, esse algoritmo é usado para resolver problemas de classificação. A categorização é feita usando algumas técnicas como Gini, Qui-quadrado, entropia etc.
Vamos considerar uma população de pessoas e usar algoritmo de árvore de decisão para identificar quem gosta de ter um cartão de crédito. Por exemplo, considere a idade eo estado civil como propriedades da população. Se idade> 30 ou uma pessoa é casada, as pessoas tendem a preferir cartões de crédito muito e menos de outra forma.

Esta árvore de decisão pode ser ampliada por meio da identificação de propriedades adequadas para definir mais categorias. Neste exemplo, se uma pessoa é casada e tem mais de 30 anos, é mais provável que tenham cartões de crédito (100% de preferência). Testar dados é usado para gerar esta árvore de decisão.

Uma árvore de decisão é uma ferramenta de suporte à decisão que usa um gráfico ou modelo de decisões em árvore e suas possíveis conseqüências, incluindo resultados do evento casual, custos de recursos e utilidade. Dê uma olhada na imagem para ter uma idéia de como ela é.


Árvore de decisão
De um ponto de vista de decisão de negócios, uma árvore de decisão é o número mínimo de perguntas sim/não que um tem que perguntar, para avaliar a probabilidade de fazer uma decisão correta, a maior parte do tempo. Como método, permite abordar o problema de forma estruturada e sistemática para chegar a uma conclusão lógica.

# K-Means
Este é um algoritmo sem supervisão que fornece uma solução para o problema de agrupamento. O algoritmo segue um procedimento para formar clusters que contêm pontos de dados homogêneos.
O valor de k é uma entrada para o algoritmo. Com base nisso, o algoritmo seleciona k número de centroides. Em seguida, os pontos de dados vizinhos para um centróide se combinam com o centroide e criam um cluster. Mais tarde, um novo centróide é criado dentro de cada cluster. Em seguida, os pontos de dados próximos ao novo centróide serão combinados novamente para expandir o cluster. Esse processo é continuado até que os centroides não mudem.

# Floresta aleatoria
A floresta aleatória pode ser identificada como uma coleção de árvores de decisão como o próprio nome diz. Cada árvore tenta estimar uma classificação e isso é chamado como “voto”. Idealmente, consideramos cada voto de cada árvore e escolhemos a classificação mais votada.

# Baias ingenuas
Este algoritmo baseia-se no “Teorema de Bayes” em probabilidade. Devido a isso, Naive Bayes só pode ser aplicado se os recursos forem independentes um do outro, pois é um requisito no teorema de Bayes. Se tentarmos prever um tipo de flor por seu comprimento e largura de pétala, podemos usar a abordagem Naive Bayes uma vez que ambos os recursos são independentes.
O algoritmo Naive Bayes também cai no tipo de classificação. Este algoritmo é usado principalmente quando existem muitas classes no problema.
Os classificadores Naïve Bayes são uma família de simples classificadores probabilísticos baseados na aplicação do teorema de Bayes com forte (naïve) independência suposições entre os recursos. A imagem em destaque é a equação – com P(A|B) é a probabilidade posterior, P(B|A) é probabilidade, P(A) é a probabilidade anterior da classe, e P(B) é preditor de probabilidade anterior.

Alguns exemplos do mundo real são:
– Marcar um e-mail como spam ou não spam
– Classificar um artigo de notícias sobre tecnologia, política ou esporte
– Verificar um pedaço de texto que expresse emoções positivas ou emoções negativas?
– Usado para software de reconhecimento de rosto.

# Algoritmos de reducao dimensional
Alguns conjuntos de dados podem conter muitas variáveis ​​que podem ser muito difíceis de manipular. Especialmente hoje, a coleta de dados em sistemas ocorre em um nível muito detalhado, devido à existência de recursos que sejam suficientes. Nesses casos, os conjuntos de dados podem conter milhares de variáveis ​​e a maioria delas pode ser desnecessária também.
Neste caso, é quase impossível identificar as variáveis ​​que têm o maior impacto em nossa previsão. Algoritmos de redução dimensional são utilizados neste tipo de situações. Ele utiliza outros algoritmos como Random Forest, Decision Tree para identificar as variáveis mais importantes.

# Algoritmos de aumento de gradiente
Gradient Boosting Algorithm usa vários algoritmos fracos para criar um algoritmo preciso mais poderoso. Em vez de usar um único estimador, ter múltiplos criará um algoritmo mais estável e robusto.
Existem vários Algoritmos de Gradient Boosting.
XGBoost — usa algoritmos de linha e árvore
LightGBM — usa apenas algoritmos baseados em árvores
A especialidade dos Algoritmos de Gradient Boosting é a sua maior precisão.Além disso, algoritmos como o LightGBM também apresentam alto desempenho incrível.

# Metodos do Ensemble
os métodos do Ensemble são algoritmos de aprendizado que constroem um conjunto de classificadores e depois classificam novos pontos de dados tomando um voto ponderado de suas previsões. O método de conjunto original é a média Bayesiana, mas os algoritmos mais recentes incluem correção de erros, codificação de saída, empacotamento e aumento.

Então, como funcionam os métodos de conjunto e por que eles são superiores aos modelos individuais?
– Diminuem os seus preconceitos: se você fizer uma série de pesquisas policiais democráticas e de pesquisas republicanas, você terá uma média de algo que não está inclinando-se de qualquer maneira.
– Reduzem a variância: a opinião agregada de um monte de modelos é menos barulhenta do que a opinião única de um dos modelos. Em finanças, isso é chamado de diversificação – um portfólio misto de muitas ações será muito menos variável do que apenas uma das ações isoladas. É por isso que seus modelos serão melhores com mais pontos de dados do que menos.

– É improvável que se ajustem excessivamente: se você possui modelos individuais que não se encaixam e você está combinando as previsões de cada modelo de forma simples (média, média ponderada, regressão logística), então não há espaço para excesso de ajuste.
Aprendizagem não supervisionada.


# Agregacao de Algoritmos
Agregação é a tarefa de agrupar um conjunto de objetos, de modo que os objetos no mesmo grupo (cluster) sejam mais parecidos entre si que aqueles em outros grupos.

Todo algoritmo de agrupamento é diferente, e aqui estão alguns deles:
– Algoritmos baseados em Centroid
– Algoritmos baseados em conectividade
– Algoritmos baseados em densidade
– Probabilística
– Redução de Dimensionalidade
– Redes Neurais/Aprendizagem Profunda


# Analise de Componentes Principais
ACP é um procedimento estatístico que usa uma transformação ortogonal para converter um conjunto de observações de variáveis possivelmente correlacionadas em um conjunto de valores de variáveis linearmente não correlacionadas chamadas componentes principais.

Algumas das aplicações do ACP incluem compressão, simplificando dados para facilitar a aprendizagem, a visualização. Observe que o conhecimento do domínio é muito importante ao escolher se deseja prosseguir com o ACP ou não. Não é adequado nos casos em que os dados são ruidosos (todos os componentes do ACP têm uma variação bastante alta).


# Decomposicao de valores singulares
na álgebra linear, DVS é uma factorização de uma matriz complexa real. Para uma dada m * n matriz M, existe uma decomposição tal que M = UΣV, onde U e V são matrizes unitárias e Σ é uma matriz diagonal.

O ACP é realmente uma simples aplicação de DVS. Na visão por computador, os primeiros algoritmos de reconhecimento de face usaram ACP e DVS para representar faces como uma combinação linear de “eigenfaces”, fazer redução de dimensionalidade e, em seguida, combinar faces para identidades através de métodos simples; embora os métodos modernos sejam muito mais sofisticados, muitos ainda dependem de técnicas similares.


# Analise de Componentes Independentes
ACI é uma técnica estatística para revelar fatores ocultos que estão subjacentes a conjuntos de variáveis, medidas ou sinais aleatórios. A ACI define um modelo generativo para os dados multivariados observados, que normalmente é dado como um grande banco de dados de amostras. No modelo, as variáveis de dados são assumidas como misturas lineares de algumas variáveis latentes desconhecidas, e o sistema de mistura também é desconhecido. As variáveis latentes são assumidas não gaussianas e mutuamente independentes, e são chamadas de componentes independentes dos dados observados.



O ACI está relacionado ao ACP, mas é uma técnica muito mais poderosa que é capaz de encontrar os fatores subjacentes das fontes quando esses métodos clássicos falham completamente. Suas aplicações incluem imagens digitais, bancos de dados de documentos, indicadores econômicos e medidas psicométricas.

<!--You can use the [editor on GitHub](https://github.com/Clalloures/Machine-Learning/edit/master/README.md) to maintain and preview the content for your website in Markdown files.
  Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.
  ### Markdown
    Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for
```markdown
Syntax highlighted code block
# Header 1
## Header 2
### Header 3
- Bulleted
- List
1. Numbered
2. List
**Bold** and _Italic_ and `Code` text
[Link](url) and ![Image](src)
```
For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
### Jekyll Themes
Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Clalloures/Machine-Learning/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.
### Support or Contact
Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out. -->
