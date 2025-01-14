import numpy as np


def shell_sort(vetor):
    intervalo = len(vetor) // 2  # Define o intervalo inicial, começando pela metade do tamanho do vetor

    # Enquanto o intervalo for maior que zero, continua o processo de ordenação
    while intervalo > 0:

        for i in range(intervalo, len(vetor)):  # Loop para iterar sobre os elementos do vetor começando pelo índice do intervalo

            temp = vetor[i]
            j = i

            # Compara os elementos à distância do intervalo e move os elementos maiores para a direita
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]  # Desloca o elemento maior
                j -= intervalo

            # Coloca o valor armazenado na posição correta
            vetor[j] = temp

        # Reduz o intervalo pela metade a cada iteração
        intervalo //= 2

    return vetor


v = shell_sort(np.array([2, 9, 3, 1, 8, 4, 7]))
print(v)