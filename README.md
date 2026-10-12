# RSA — Implementação Didática e Análise de Algoritmos

## 1. Sobre o projeto

Este projeto tem como objetivo estudar, implementar e analisar os fundamentos matemáticos e computacionais do algoritmo criptográfico **RSA (Rivest–Shamir–Adleman)**, um dos criptossistemas de chave pública mais conhecidos da criptografia moderna.

O desenvolvimento é realizado em **Python**, priorizando a compreensão dos algoritmos e das propriedades da Teoria dos Números que fundamentam seu funcionamento.

Diferentemente de uma implementação voltada ao uso comercial, este projeto adota uma abordagem didática e investigativa. Os algoritmos são implementados individualmente, documentados e submetidos a testes automatizados antes de serem integrados ao criptossistema.

Além da implementação funcional do RSA, o projeto busca investigar a eficiência computacional de diferentes estratégias para resolver problemas matemáticos equivalentes, utilizando análise assintótica e experimentos de desempenho.

### Objetivos

- Implementar algoritmos fundamentais da Teoria dos Números em Python.
- Compreender e aplicar propriedades matemáticas relacionadas à criptografia RSA.
- Desenvolver um criptossistema RSA didático com codificação e decodificação de mensagens.
- Investigar diferentes implementações para um mesmo problema matemático.
- Determinar a complexidade temporal e espacial dos algoritmos utilizando as notações $O$, $\Omega$ e $\Theta$.
- Comparar experimentalmente o desempenho das implementações.
- Relacionar os resultados teóricos aos resultados experimentais.

> **Aviso:** este projeto possui finalidade exclusivamente educacional. A implementação utiliza RSA sem os mecanismos de segurança necessários para aplicações reais, como padding criptográfico seguro e geração de chaves com parâmetros apropriados. Não deve ser utilizada para proteger informações sensíveis.

---

## 2. Fundamentação matemática

O RSA utiliza propriedades da aritmética modular, dos números primos e das funções aritméticas para construir um sistema de criptografia assimétrica.

Sua fundamentação envolve, entre outros conceitos:

- Divisibilidade, números primos e máximo divisor comum.
- Algoritmo de Euclides e Identidade de Bézout.
- Congruências e inversos multiplicativos modulares.
- Função totiente de Euler e Teorema de Euler.
- Função de Carmichael e seu teorema correspondente.
- Exponenciação modular e propriedades das classes residuais.

A implementação contempla duas abordagens para a geração de chaves RSA: uma baseada na função totiente de Euler e outra baseada na função de Carmichael.

### 2.1. Geração de chaves pelo totiente de Euler

Dados dois números primos distintos $p$ e $q$, calcula-se:

$$
N = pq
$$

$$
\varphi(N) = (p-1)(q-1)
$$

Escolhe-se um expoente público $e$ coprimo com $\varphi(N)$, e determina-se o expoente privado $d$ pela congruência:

$$
ed \equiv 1 \pmod{\varphi(N)}
$$

### 2.2. Geração de chaves pela função de Carmichael

Alternativamente, podemos utilizar:

$$
\lambda(N) = \operatorname{lcm}(p-1,q-1)
$$

Nesse caso, o expoente privado satisfaz:

$$
ed \equiv 1 \pmod{\lambda(N)}
$$

Ambas as abordagens produzem pares de chaves matematicamente válidos para o RSA didático desenvolvido neste projeto.

### 2.3. Criptografia e descriptografia

A chave pública é representada pelo par $(N,e)$, enquanto a chave privada é representada por $(N,d)$.

Para uma mensagem numérica $M$, com $0 \leq M < N$, a criptografia é realizada por:

$$
C = M^e \bmod N
$$

A descriptografia utiliza:

$$
M = C^d \bmod N
$$

Essas operações são executadas por meio de exponenciação modular rápida.

---

## 3. Algoritmos implementados

O projeto reúne implementações de diferentes algoritmos matemáticos, incluindo versões alternativas para permitir comparações de complexidade e desempenho.

### 3.1. Teoria dos Números

| Módulo | Algoritmos |
|---|---|
| `gcd.py` | Algoritmo de Euclides |
| `extended_gcd.py` | Euclides Estendido: duas versões iterativas e uma recursiva |
| `lcm.py` | Mínimo múltiplo comum |
| `totient.py` | Totiente de Euler: contagem por MDC e fatoração prima |
| `carmichael.py` | Função de Carmichael por fatoração prima |
| `primality.py` | Divisão por tentativa: tradicional, divisores ímpares e candidatos $6k\pm1$ |
| `modular_exponentiation.py` | Exponenciação modular linear e rápida |
| `modular_inverse.py` | Inversão modular por Euclides Estendido e Teorema de Euler |

No total, foram selecionadas **15 implementações** para a análise assintótica individual.

### 3.2. Criptossistema RSA

| Módulo | Responsabilidade |
|---|---|
| `key_generation.py` | Geração de chaves utilizando Euler ou Carmichael |
| `message_encoding.py` | Codificação textual, divisão e reconstrução de blocos |
| `encryption.py` | Criptografia dos blocos numéricos |
| `decryption.py` | Descriptografia e recuperação da mensagem |

### 3.3. Codificação de mensagens

Para simplificar a representação de mensagens, foi desenvolvido um sistema didático de codificação decimal.

Cada letra maiúscula recebe um código de dois algarismos:

$$
A=10,\quad B=11,\quad C=12,\quad \ldots,\quad Z=35
$$

Os códigos são concatenados e divididos em blocos numéricos menores que o módulo RSA.

Cada bloco é criptografado individualmente e, após a descriptografia, os códigos são reconstruídos para recuperar a mensagem original.

A versão atual aceita letras maiúsculas de `A` até `Z`, sem espaços ou caracteres especiais.

---

## 4. Organização do projeto

O código está organizado de maneira modular, separando os algoritmos matemáticos das operações específicas do RSA.

```text
number_theory/
    carmichael.py
    extended_gcd.py
    gcd.py
    lcm.py
    modular_exponentiation.py
    modular_inverse.py
    primality.py
    totient.py

rsa/
    decryption.py
    encryption.py
    key_generation.py
    message_encoding.py

tests/
    ... testes automatizados ...

main.py
README.md
```

A pasta `number_theory` contém algoritmos matemáticos reutilizáveis. A pasta `rsa` reúne as funcionalidades necessárias para construir o criptossistema.

Os testes são mantidos separadamente do código principal, seguindo práticas de modularização e testes automatizados.

---

## 5. Testes e validação

As implementações são verificadas utilizando o framework **pytest**.

Os testes foram desenvolvidos considerando técnicas de engenharia de software e propriedades matemáticas, incluindo:

- Particionamento em classes de equivalência.
- Análise de valores-limite.
- Testes de exceções e entradas inválidas.
- Comparação entre implementações equivalentes.
- Verificação de identidades e propriedades matemáticas.
- Testes de integração entre geração de chaves, criptografia e descriptografia.

Um dos principais testes de integração verifica a recuperação da mensagem original após a criptografia:

$$
D_{\text{privada}}\big(E_{\text{pública}}(M)\big)=M
$$

As implementações também são submetidas a testes individuais para verificar seus resultados e comportamentos esperados.

Para executar a suíte de testes, a partir da raiz do projeto, com o ambiente e as dependências configurados:

```bash
python -m pytest -v
```

Os testes automatizados ajudam a identificar erros e verificar propriedades esperadas, mas não substituem as demonstrações matemáticas de correção.

---

## 6. Metodologia de análise de algoritmos

A próxima etapa do projeto consiste na investigação formal da complexidade computacional das 15 implementações selecionadas.

A análise será desenvolvida a partir de um modelo de custo previamente definido, tomando como referência inicial o **modelo RAM de custo uniforme**.

Para cada algoritmo, pretende-se:

1. Identificar os parâmetros que caracterizam o tamanho da entrada.
2. Definir as operações elementares e seus respectivos custos.
3. Contabilizar as frequências de execução das instruções.
4. Construir uma função de custo representativa.
5. Investigar os melhores e piores casos de execução.
6. Demonstrar os limites assintóticos por meio das notações $O$, $\Omega$ e $\Theta$.
7. Determinar a complexidade espacial auxiliar.

As demonstrações considerarão as características específicas das implementações.

Será feita também uma distinção entre a análise baseada em operações aritméticas de custo constante e os custos associados à representação binária de inteiros grandes, particularmente relevantes para algoritmos criptográficos.

**Estado atual:** metodologia em planejamento; contagens e demonstrações formais ainda não concluídas.

---

## 7. Análise experimental de desempenho

Após a análise teórica, serão realizados experimentos para comparar o desempenho das implementações.

Os principais grupos de comparação serão:

| Problema | Implementações |
|---|---|
| Algoritmo de Euclides Estendido | 3 versões |
| Função totiente de Euler | 2 versões |
| Teste de primalidade | 3 versões |
| Exponenciação modular | 2 versões |
| Inverso multiplicativo modular | 2 versões |

Os experimentos buscarão investigar como os tempos de execução variam em função do tamanho e das características matemáticas das entradas.

A metodologia experimental deverá contemplar medições repetidas, controle das condições de execução, registro dos resultados e construção de gráficos comparativos.

Os dados serão armazenados em arquivos estruturados, possibilitando análises posteriores e reprodução dos experimentos.

O objetivo não será apenas identificar a implementação mais rápida em determinado experimento, mas **compreender a relação entre a complexidade teórica, a estrutura dos algoritmos e seu desempenho observado**.

**Estado atual:** benchmarks ainda não realizados.

---

## 8. Estado de desenvolvimento

| Etapa | Situação |
|---|---|
| Implementação dos algoritmos matemáticos | Concluída |
| Implementação do RSA didático | Concluída |
| Codificação e decodificação de mensagens | Concluída |
| Testes automatizados iniciais | Concluídos |
| Análise assintótica formal | Planejada |
| Instrumentação e benchmarks | Planejados |
| Gráficos e interpretação dos resultados | Planejados |
| Documentação técnica e matemática completa | Em desenvolvimento |

Este README representa uma versão inicial da documentação e será atualizado conforme o avanço das análises.

---

## 9. Referências teóricas

As seguintes obras constituem referências iniciais para a fundamentação matemática e computacional do projeto:

- CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. *Introduction to Algorithms*. MIT Press.
- KNUTH, D. E. *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*. Addison-Wesley.
- BACH, E.; SHALLIT, J. *Algorithmic Number Theory, Volume 1: Efficient Algorithms*. MIT Press.
- MENEZES, A. J.; VAN OORSCHOT, P. C.; VANSTONE, S. A. *Handbook of Applied Cryptography*. CRC Press.

As referências serão ampliadas e detalhadas durante a elaboração das demonstrações e da documentação final.

---

## 10. Considerações finais

Este projeto procura integrar conceitos de **Teoria dos Números, Álgebra, Criptografia e Análise de Algoritmos** por meio da implementação computacional de resultados matemáticos.

Além de construir um criptossistema RSA funcional para fins didáticos, pretende-se investigar como diferentes algoritmos podem solucionar o mesmo problema, apresentando características distintas de complexidade e desempenho.

O código constitui a base prática de um estudo mais amplo, que poderá ser posteriormente expandido e incorporado a um trabalho acadêmico sobre os fundamentos matemáticos do RSA.

**O projeto encontra-se em desenvolvimento, com foco atual na formalização da análise de complexidade e na preparação dos experimentos computacionais.**
