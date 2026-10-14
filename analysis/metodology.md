# Metodologia de Análise de Complexidade

## 1. Modelo computacional adotado

Para a análise teórica dos algoritmos, adotou-se o **modelo RAM de custo uniforme (*Uniform-Cost Random Access Machine*)**, no qual as operações elementares possuem custo constante, independentemente dos valores dos operandos.

A análise será realizada por meio da contagem de operações elementares executadas por cada algoritmo, considerando a estrutura de controle e as características das entradas.

A função de custo será expressa por:

$$
T(n)=\sum_{i=1}^{k}c_i r_i(n)
$$

Em que:

- $c_i$ representa o custo atribuído à operação de índice $i$.
- $r_i(n)$ representa sua frequência de execução.
- $k$ corresponde ao número de instruções ou grupos de operações analisados.

Para algoritmos com múltiplos parâmetros, a função de custo será expressa em termos de todas as variáveis relevantes.

## 2. Convenção de custos elementares

A seguinte convenção será utilizada uniformemente nas análises.

| Operação | Custo |
|---|---|
| Atribuição (`=`, `+=`, `//=`) | 1 pela escrita, acrescido dos custos da expressão |
| Soma, subtração, multiplicação | 1 |
| Divisão inteira (`//`) | 1 |
| Resto (`%`) | 1 |
| Comparação (`<`, `==`, `<=`, etc.) | 1 |
| Operação lógica efetivamente avaliada | 1 |
| Acesso ou indexação em lista | 1 |
| `append()` | 1 amortizado |
| Chamada de função auxiliar | Custo da função chamada |
| `return` | 1 |

Instruções compostas terão seus custos determinados pela soma das operações elementares efetivamente executadas.

As expressões booleanas seguirão a avaliação de curto-circuito da linguagem Python, distinguindo os caminhos de execução quando necessário.

As condições dos laços serão contabilizadas incluindo sua última avaliação, responsável pelo encerramento da repetição.

Para chamadas de funções auxiliares, será considerado o custo das operações realizadas pela função chamada, evitando tratar algoritmos não constantes como operações elementares.

## 3. Convenções adicionais

A contagem será realizada sobre os caminhos de execução efetivamente percorridos, distinguindo entradas válidas, entradas inválidas e casos de fronteira.

As funções de custo poderão depender de parâmetros auxiliares, como o número de iterações de um laço, que posteriormente serão relacionados ao tamanho e às propriedades da entrada.

Na análise espacial, distinguiremos a memória auxiliar utilizada pelo algoritmo do espaço necessário para armazenar suas entradas e saídas.

O modelo de custo uniforme será utilizado na análise principal. Entretanto, como os algoritmos trabalham com inteiros arbitrariamente grandes, suas limitações serão explicitadas. Quando pertinente, será discutida a complexidade em bits, que considera o custo computacional das operações aritméticas em função do tamanho binário dos operandos.

## 4. Notações assintóticas

Após a construção das funções de custo, serão determinados e demonstrados, quando aplicáveis, limites assintóticos utilizando as notações:

- $O(g(n))$: limite superior assintótico.
- $\Omega(g(n))$: limite inferior assintótico.
- $\Theta(g(n))$: limite assintótico justo.

Serão analisados os melhores e piores casos conforme as características das entradas. O caso médio será considerado apenas quando houver uma distribuição de probabilidade explicitamente definida.

As demonstrações deverão apresentar as hipóteses utilizadas, a relação entre os parâmetros de entrada e as constantes necessárias às definições formais das notações assintóticas.

## 5. Reprodutibilidade

Todas as análises individuais deverão utilizar as convenções descritas neste documento.

Quaisquer simplificações, hipóteses adicionais ou alterações na unidade de custo deverão ser explicitamente documentadas, garantindo que as comparações entre implementações permaneçam coerentes.