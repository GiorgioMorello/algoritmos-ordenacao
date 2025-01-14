import numpy as np



def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):

        # Inicializa o índice do menor valor como o valor atual de i
        indice_menor = i
        for j in range(i + 1, n):
            if vetor[indice_menor] > vetor[j]:
                indice_menor = j  # Atualiza o índice do menor valor

        # Realizando as trocas dos elementos
        temp = vetor[i]

        # Coloca o valor encontrado como o menor (vetor[indice_menor]) na posição atual (vetor[i])
        vetor[i] = vetor[indice_menor]

        # Coloca o valor original de vetor[i] (armazenado em 'temp') na posição de vetor[indice_menor], completando a troca
        vetor[indice_menor] = temp

    return vetor


v = selection_sort(np.array([2, 9, 3, 1, 8, 4, 7]))
print(v)