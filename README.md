# Algoritmos de Ordenação em Python

### Algoritmos Implementados
  * Bubble Sort
  * Selection Sort
  * Insertion Sort
  * Merge Sort
  * Quick Sort
  * Shell Sort



## Bubble Sort
#### O Bubble Sort é o algoritmo de ordenação mais simples e notavelmente mais lento. 
#### Seu funcionamento é da seguinte forma
  *  É feito a comparação de dois números.
  *  Se o número da esquerda for maior, os elementos devem ser trocados.
  *  Desloca-se uma posição à direita.
  *  O algoritmo vai deslocando os maiores valores para direita.

 Em um vetor com 10 elementos será feito 45 comparações: $~$  9+8+7+6+5+4+3+2+1 = 45 <br />
 Sua notação Big-O é de O(n²) -> Função quadratica
<br /><br />


## Selection Sort
#### O Selection Sort melhora a ordenação pelo método da bolha reduzindo o número de trocas necessárias de N² para N.
#### Funcionamento
  *  Percorre todos os elementos e seleciona o menor.
  *  O menor elemento é trocado com o elemento da extremidade esquerda do vetor(posições iniciais)
  *  É feito uma troca somente a cada rodada.
  *  Os elementos ordenados acumulam-se na esquerda
  
 Em um vetor com 10 elementos ainda será necessário 45 comparações.<br />
 Sua notação Big-O também é de O(n²). <br />
 Em um vetor de 100 elementos, são requeridas 4950 comparações e menos de 100 trocas.<br />
<br /><br />



## Insertion Sort
#### O Insertion Sort é duas vezes mais rapido que o método da bolha e um pouco mais rapido que a ordenação por seleção em situações normais(vetores com dados aleatórios).

#### Funcionamento
  *  Há um marcador em algum lugar no meio do vetor.
  *  Os elementos à esquerda do marcado estão parcialmente ordenados (estão ordenados entre eles, porém não estão em suas posições finais).
  *  Os elementos à direita do marcador não estão ordenados. 

 Sua notação Big-O também é de O(n²). <br />
 Um vetor com dados em ordem inversa(decrescente), todas as comparações e deslocamento são executados, sendo mais lento que o Bubble sort
 <br /><br />

 
## Shell Sort
#### Melhora a ordenação pelo método Insert sort, podendo ser considerado uma 'versão' Insertion sort. Esse algoritmo utiliza a técnica de "intervalo" (distância entre os elementos a serem comparados) que diminui progressivamente até que o vetor esteja completamente ordenado.

#### Funcionamento
  *  O algoritmo começa comparando elementos que estão a uma certa distância do intervalo. O intervalo é inicialmente grande e vai diminuindo a cada iteração.
  *  Esse algoritmo compara e move os elementos que estão a um intervalo maior do que 1, o que permite que os elementos sejam movidos para mais perto de suas posições finais de forma mais eficiente.
  *  O processo continua até que o intervalo seja reduzido a 1, momento em que o algoritmo executa uma versão do Insertion Sort para ordenar os elementos restantes.

 Sua notação Big-O é de O(n*log n) e no seu pior caso O(n²). <br />
 O Shell Sort é considerado um algoritmo instável porque, em alguns casos, ele pode alterar a ordem relativa dos elementos iguais durante o processo de ordenação.
 <br /><br />

 
## Merge Sort
#### O Merge Sort é faz a ordenação baseado na técnica de "Dividir e Conquistar", que divide recursivamente o vetor em partes menores até que cada parte tenha apenas um elemento e, em seguida, as mescla de forma ordenada.

#### Funcionamento
  *  O algoritmo começa dividindo o vetor original em duas metades.
  *  Cada metade é recursivamente dividida em duas partes, até que todas as partes tenham apenas um único elemento.
  *  Em seguida, começa o processo de merge: as partes menores são combinadas duas a duas, de forma ordenada, até que todas as partes sejam reunidas novamente em uma estrutura ordenada.
  *  Durante o processo de merge, os elementos de cada subvetor são comparados e os menores (ou maiores, dependendo da ordem desejada) são inseridos em uma nova lista ou vetor.

Possui a notação Big-O de O(n*log n) no melhor caso e no pior caso.
 <br /><br />


## Quick Sort

#### O Quick Sort é amplamente reconhecido como um dos algoritmos de ordenação mais rápidos e eficientes para listas grandes. Também é baseado na técnica "Dividir e Conquistar"

#### Funcionamento
  *  O algoritmo começa escolhendo um pivô (um elemento do vetor). O elemento pivô pode ser o primeiro elemento, o último, o elemento do meio ou até mesmo um pivô aleatório.
  *  O vetor é então reorganizado de tal forma que todos os elementos menores que o pivô ficam à sua esquerda, e todos os elementos maiores que o pivô ficam à sua direita. Esse processo de rearranjo é chamado de particionamento.
  *  O mesmo processo de escolha do pivô e particionamento é repetido recursivamente para as sublistas à esquerda e à direita do pivô, até que todas as sublistas estejam ordenadas.
  *  Quando as sublistas atingem tamanho 1 (ou 0), a ordenação está concluída. A ordenação final é formada pela combinação das sublistas ordenadas.


No pior caso sua notação Big-O é O(n²), isso acontece quando o elemento pivot é o maior ou menor elemento.
No melhor caso sua notação é O(n*log n).







 
