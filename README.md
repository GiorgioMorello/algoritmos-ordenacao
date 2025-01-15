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



## Selection Sort
#### O Insertion Sort é duas vezes mais rapido que o método da bolha e um pouco mais rapido que a ordenação por seleção em situações normais(vetores com dados aleatórios).

#### Funcionamento
  *  Há um marcador em algum lugar no meio do vetor.
  *  Os elementos à esquerda do marcado estão parcialmente ordenados (estão ordenados entre eles, porém não estão em suas posições finais).
  *  Os elementos à direita do marcador não estão ordenados. 

 Sua notação Big-O também é de O(n²). <br />
 Um vetor com dados em ordem inversa(decrescente), todas as comparações e deslocamento são executados, sendo mais lento que o Bubble sort
 












 
