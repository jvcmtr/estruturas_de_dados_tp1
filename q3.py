from BinaryHeap import BinaryHeap

def caso_ordenado(n=10):
    return [x for x in range(n)]


def caso_inverso(n=10):
    return [x for x in range(n - 1, -1, -1)]

# Se utilizassemos um caso aleatorio, seria nescessario diversos testes para conseguir a media
def caso_alternado(n=10):
    arr = [x for x in range(1, n+1)]
    
    for i in range(len(arr)):
        if i%2 == 0:
            arr[i] = arr[i] * -1

    return arr

def teste(name, dados):
    print("______________________________")
    print(f"    ==== Executando teste {name} ==== ")
    print(f"    - Dados : {dados}")
    print(f"    - Operações realizadas : ")
    heap = BinaryHeap(dados)
    print(f"    - Heap reultante :{heap} ")
    print()
    

if __name__ == "__main__":
    N = 7
    print(f"Exercicio 3.3 - executando testes com arrays de {N} elementos em diferentes ordenações")
    teste("Dados ordenados", caso_ordenado(N))
    teste("Dados invertidos", caso_inverso(N))
    teste("Dados alternados", caso_alternado(N))