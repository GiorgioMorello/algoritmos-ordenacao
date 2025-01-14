import numpy as np

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):

        if vetor[j] <= pivo: # Quando encontramos um valor menor  ou igual ao pivo, colocamos o elemento à esquerda
            i+=1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return i+1


def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)

        quick_sort(vetor, inicio, posicao - 1)  # Ordernar a parte esquerda do vetor

        quick_sort(vetor, posicao + 1, final)  # Ordernar a parte direita do vetor

        return vetor



vetor = np.array([10,8,1, 3, 5,9])

quick_sort(vetor, 0, len(vetor)-1)