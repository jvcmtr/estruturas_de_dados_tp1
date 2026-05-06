from Heap import Heap
import random

def gerar_dados(n=10, limite=1000):
    return [random.randint(0, limite) for _ in range(n)]


def testar_inicializacao(is_min):
    dados = gerar_dados()
    heap = Heap(dados, is_min)
    if len(heap) != len(dados):
        return f"Falha na inicialização. tipo:{'MinHeap' if is_min else 'MaxHeap'} ; conteudo:{dados}"
    return ""


def testar_pop(is_min):
    dados = gerar_dados()
    heap = Heap(dados, is_min)

    resultado = [heap.pop() for _ in range(len(heap))]
    esperado = sorted(dados, reverse=not is_min)

    if resultado != esperado:
        return ( f"Falha no pop. tipo:{'MinHeap' if is_min else 'MaxHeap'} ; conteudo:{dados}")
    return ""


def testar_validacao(is_min):
    dados = gerar_dados()
    heap = Heap(dados, is_min)

    result = testar_pop(is_min) == ""
    result_interno = heap._test()

    if result != result_interno:
        return (f"Validação interna não condiz com teste externo. tipo:{'MinHeap' if is_min else 'MaxHeap'} ; conteudo:{dados}")
    return ""


def executar_testes():
    print("_____________________________________________")
    print("Executando testes...")

    resultados = []
    for is_min in (True, False):
        resultados += [
            testar_inicializacao(is_min),
            testar_pop(is_min),
            testar_validacao(is_min),
        ]

    falhas = [x for x in resultados if x != ""]
    print("SUCESSO" if not falhas else "FALHA !")
    for f in falhas:
        print(f" - {f}")
    print("_____________________________________________")
    

if __name__ == "__main__":
    executar_testes()