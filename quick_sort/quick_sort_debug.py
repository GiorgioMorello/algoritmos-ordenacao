import numpy as np


def particao(vetor, inicio, final):
    pivo = vetor[final] # O pivô é o último elemento do vetor
    i = inicio - 1 # Inicializa o índice para a posição antes do início do vetor

    for j in range(inicio, final): # percorrer o vetor do inicio até o ultimo elemento
        if vetor[j] <= pivo:
            i+=1
            vetor[i], vetor[j] = vetor[j], vetor[i]  # Trocar os elementos para colocar os menores à esquerda do pivô

    vetor[i+1], vetor[final] = vetor[final], vetor[i+1] # Coloca r  o  elemento pivo na posição correta
    return i+1 # Retorna a posição do pivo


def quick_sort(vetor, inicio, final):
    if inicio < final:  # Verifica se ha mais de um elemento no intervalo que estamos considerando.

        posicao = particao(vetor, inicio, final)  # Realiza a partição e obtém a posição do pivô

        quick_sort(vetor, inicio, posicao - 1)  # Ordernar a parte esquerda do vetor

        quick_sort(vetor, posicao + 1, final)  # Ordernar a parte direita do vetor

        return vetor

vetor = np.array([2, 9, 3, 1, 8, 4, 7])
v = quick_sort(vetor, 0, len(vetor)-1)
print(v)