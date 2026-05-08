from BinaryHeap import BinaryHeap

def teste(name, size, rm):
    print("______________________________")
    print(f"    ==== Teste: '{name}' ==== ")
    dados = [x for x in range(size)]
    heap = BinaryHeap(dados)
    print(f"    - Heap original: {heap}")
    print(f"    - Item a ser removido : {rm}")
    heap.delete(rm)
    print(f"    - Heap resultante : {heap}") 
    print(f"    - Heap valida? {heap._test()}") 


if __name__ == "__main__":
    teste(" Remoção de item existente", 9, 4)
    teste(" Remoção de item inexistente", 9, 12)