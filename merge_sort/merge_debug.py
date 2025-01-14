import numpy as np


def merge_sort(vetor):
    if len(vetor) > 1:  # Ponto de parada
        half = len(vetor) // 2
        first_half = vetor[:half].copy()
        second_half = vetor[half:].copy()

        # print(first_half, 'first')
        # print(second_half, 'second')

        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0

        # Ordenar a esquerda e direita

        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                vetor[k] = first_half[i]
                i += 1
            else:
                vetor[k] = second_half[j]
                j += 1

            k += 1

        # Ordenação final
        while i < len(first_half):
            vetor[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            vetor[k] = second_half[j]
            j += 1
            k += 1


    return vetor


v = merge_sort(np.array([10, 9, 3, 7, 5]))