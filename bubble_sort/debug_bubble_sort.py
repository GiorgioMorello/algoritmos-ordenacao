import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):  # A cada iteração, o maior elemento é colocado na posição correta

            if vetor[j] > vetor[j + 1]:  # Compara elementos adjacentes e troca se estiverem na ordem errada

                # Troca os elementos de posição
                temp = vetor[j]

                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor



v = bubble_sort(np.array([2, 9, 3, 1, 8, 4, 7]))
print(v)