# Algoritmos de triangulação de polígonos

## Remoção de orelhas

O algoritmo de remoção de orelhas triangula o polígono removendo as orelhas, uma por uma.
Marca todas as orelhas num pré-processamento.

Para decidir se um vértice é ponta de uma orelha, verifica se a diagonal de seus vizinhos
está em seu cone e se não intersecta com nenhuma outra aresta.

Implementado com listas ligadas, consome tempo O(n^2).

### Animação

A maior parte da animação é composta de chamadas a operação esquerda, representada por
triângulos amarelos. São provenientes das primitivas NoCone e QuaseDiagonal.

Um vértice que é uma ponta de orelha é marcado como verde.

Uma diagonal da triangulação é verde.

## Y-Monótono

## Lee e Preparata

O algoritmo de Lee e Preparata particiona o polígono em vários polígonos y-monótonos. Depois triangula-se
cada uma das partes com o algoritmo descrito anteriormente.

A partição é criada por um método de linha de varredura. Os pontos eventos são vértices do polígono. Iteramos pelos vértices do maior para o menor y
(em caso de empate, pegamos o vértice de menor x). O algoritmo implementado é descrito na seção 3.2 do livro de Berg [1].

Uma árvore de busca binária, ou ABB, é usada para representar a linha de varredura. A árvore escolhida foi uma Treap, uma árvore com esquema
de balanceamento aleatorizado. Apesar da árvore guardar segmentos, pontos são usados na inserção e remoção. O ponto usado é sempre o ponto
evento corrente.

A partição é representada por uma lista de arestas duplamente encadeada, ou DCEL. Inicialmente se cria uma DCEL com as arestas do polígono. As diagonais vão sendo
adicionadas conforme vão sendo encontradas. Para adicionar a diagonal vw, itera-se por todas meias-arestas que saem de w e por todas meias-arestas que saem de v. Em geral esse processo pode consumir muito tempo, mas pode-se provar que no caso da partição em polígonos y-monótonos cada vértice tem no máximo 6 meias-arestas que saem dele. Portanto a inserção na DCEL é constante.

### Animação

A linha de varredura é a linha verde que desce pelo polígono. 

Os triângulos amarelos representam testes de esquerda provenientes de comparações na ABB. 

Um triângulo azul claro é um teste de esquerda realizado na identificação de um vértice (se é ponta para cima ou para baixo).

Arestas roxas são arestas do polígono que fazem parte da linha de varredura.

Diagonais brancas são as diagonais da partição em polígonos monótonos (que também fazem parte da triangulação).

Diagonais verdes são as outras diagonais da triangulação, inseridas pelo algoritmo de y-monótono.

### Referências

[1] Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars. 2008. Computational Geometry: Algorithms and Applications (3rd ed. ed.). TELOS, Santa Clara, CA, USA.

## Etc

O número que aparece ao lado do nome dos algoritmos é o número de chamadas à primitiva area2. Apesar de parecer determinístico, o algoritmo de Lee e Preparata tem um número variado, pois a ABB usada possui um esquema de balanceamento aleatório.
