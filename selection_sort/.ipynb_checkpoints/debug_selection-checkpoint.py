import numpy as np


def selection_sort(vetor):
    n = vetor.capacidade

    for i in range(n):

        menor = i
        for j in range(i + 1, n):
            if vetor.valores[menor] > vetor.valores[j]:
                menor = j

        temp = vetor.valores[i]
        vetor.valores[i] = vetor.valores[menor]
        vetor.valores[menor] = temp

    return vetor


# Vetor não ordenado

class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_pos = -1  # Iremos incrementar esse atributo a cada vez que adicionarmos um valor na array
        self.valores = np.empty(self.capacidade,
                                dtype=int)  # Retorna um array baseado no formato e no tipo que você passar

    # O(n)
    def listar_valores(self):
        if self.ultima_pos == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultima_pos + 1):
                print(i, '-', self.valores[i])

    # O(1) - O(2), independente do valor que passarmos, o número de passos será o mesmo
    def inserir(self, valor):
        if self.ultima_pos == self.capacidade - 1:
            print('capacidade maxima atingida')
        else:
            self.ultima_pos += 1
            self.valores[self.ultima_pos] = valor

    # O(n) -> Ele vai executar linearmente de acordo com as entradas que você passar
    def pesquisar_valor(self, valor):
        for i in range(self.ultima_pos + 1):
            if valor == self.valores[i]:
                return i
        return -1

    # O(n)
    def excluir_valor(self, valor):
        indice_valor = self.pesquisar_valor(valor)
        if indice_valor != -1:

            for i in range(indice_valor, self.ultima_pos):
                self.valores[i] = self.valores[i + 1]
            self.ultima_pos -= 1

        else:
            print('Valor não encontrado')
            return -1



v = VetorNaoOrdenado(5)
v.inserir(5)
v.inserir(4)
v.inserir(3)
v.inserir(2)
v.inserir(1)

v.listar_valores()
print('-'*8)
selection_sort(v).listar_valores()