import numpy as np


def insertion_sort(vetor):
    n = len(vetor)  # Definindo tamanho do vetor

    for i in range(1, n):  # Inicia o loop a partir do segundo elemento até o final do vetor
        valor_atual = vetor[i]

        j = i - 1  # O índice 'j' começa na posição anterior à de i, para comparar com os elementos à esquerda

        # Enquanto o valor_atual for menor que o valor à esquerda e o índice j for válido
        while j >= 0 and valor_atual < vetor[j]:
            vetor[j + 1] = vetor[j]  # Move o elemento à esquerda para a posição à direita

            j -= 1  # Decrementa 'j' para comparar com o próximo elemento à esquerda

        vetor[j + 1] = valor_atual  # Coloca o valor_atual na posição correta
    return vetor



v = insertion_sort(np.array([2, 9, 3, 1, 8, 4, 7]))
print(v)