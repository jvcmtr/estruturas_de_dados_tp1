from BinaryHeap import BinaryHeap
import math

def altura(n):
    return math.ceil(math.log2(n + 1)) - 1

def teste(name, dados):
    print("______________________________")
    print(f"    ==== Executando teste {name} ==== ")
    heap = BinaryHeap(dados)
    while not heap.peek() == None: 
        # print(f"    ________")
        print(f"    - Heap atual : {heap}")
        print(f"      Altura da arvore : {altura(len(heap))}")
        print(f"      Item a ser removido: {heap.peek()}")
        if altura(len(heap)) >= 2:
            print(f"      Operações realizadas: ")
        i = heap.pop()
    
    print("Heap vazia")
    print()

if __name__ == "__main__":
    N = 8
    dados = [x for x in range(N)]
    teste("Remoção de itens", dados)