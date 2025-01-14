import numpy as np


def merge_sort(vetor):
    if len(vetor) > 1:  # Critério de parada: o vetor tem um ou nenhum elemento

        mid = len(vetor) // 2  # Definindo o índice do meio
        left_half = vetor[:mid].copy()  # Cria uma cópia da primeira metade do vetor
        right_half = vetor[mid:].copy()  # Cria uma cópia da segunda metade do vetor

        # Ordena as duas metades recursivamente
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa os índices para as partes esquerda, direita e para o vetor original
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # Se o elemento da esquerda for menor
                vetor[k] = left_half[i]  # Coloca o elemento da esquerda no vetor
                i += 1

            else:
                vetor[k] = right_half[j]  # Caso contrário, coloca o elemento da direita no vetor
                j += 1
            k += 1  # Avança uma posição no vetor original

        # Se ainda houver elementos na metade esquerda, coloca-os no vetor
        while i < len(left_half):
            vetor[k] = left_half[i]
            i += 1
            k += 1

        # Se ainda houver elementos na metade direita, coloca-os no vetor
        while j < len(right_half):
            vetor[k] = right_half[j]
            j += 1
            k += 1

    return vetor


v = merge_sort(np.array([2, 9, 3, 1, 8, 4, 7]))
print(v)