from BinaryHeap import BinaryHeap

# Exercicio 7.1
def is_valid_heap(array, idx=0):
    for i in range(len(array)):
        l = i*2+1
        r = i*2+2

        # Se um filho é mais prioritario que o pai, retorna falso 
        if r <= len(array)-1 and array[r] < array[i]:  
            return False
        if l <= len(array) -1 and array[l] < array[i]:
            return False
    return True


if __name__ == "__main__":
    print("_______________________")
    print(" === Teste com array valido === ")
    arr = [x for x in range(1, 10)]
    print("array: ",arr)
    print("retorno de is_valid_heap : ", is_valid_heap(arr))

    print("_______________________")
    print(" === Teste com array invalido === ")
    arr = [x for x in range(1, 10)]
    arr[0] = 200
    print("array: ", arr)
    print("retorno de is_valid_heap : ", is_valid_heap(arr))