from BinaryHeap import BinaryHeap
import random

def gerar_dados(n=10, limite=1003):
    return [random.randint(0, limite) for _ in range(n)]

def tipo(m):
    return f"tipo:{'MinHeap' if m else 'MaxHeap'}" 


def testar_inicializacao(is_min):
    dados = gerar_dados()
    heap = BinaryHeap(dados, is_min)
    if len(heap) != len(dados):
        return f"Falha na inicialização. {tipo(is_min)} ; conteudo:{dados}"
    return ""


def testar_pop(is_min):
    dados = gerar_dados()
    heap = BinaryHeap(dados, is_min)

    resultado = [heap.pop() for _ in range(len(heap))]
    esperado = sorted(dados, reverse=not is_min)

    if resultado != esperado:
        return ( f"Falha no pop. {tipo(is_min)} ; conteudo:{dados}")
    return ""


def testar_validacao(is_min):
    dados = gerar_dados()
    heap = BinaryHeap(dados, is_min)

    result = testar_pop(is_min) == ""
    result_interno = heap._test()

    if result != result_interno:
        return (f"Validação interna não condiz com teste externo. {tipo(is_min)} ; conteudo:{dados}")
    return ""


def executar_testes():
    print("Executando testes...")

    resultados = []
    for is_min in (True, False):
        resultados += [
            testar_inicializacao(is_min),
            testar_pop(is_min),
            testar_validacao(is_min),
        ]

    falhas = [x for x in resultados if x != ""]
    print(f"{len(resultados) - len(falhas)} de {len(resultados)} testes bem sucedidos")
    print("SUCESSO" if not falhas else "FALHA !")
    for f in falhas:
        print(f" - {f}")
    

if __name__ == "__main__":
    executar_testes()