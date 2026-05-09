

class BinaryHeap:
    def __init__(self, data = [], is_min=True):
        # Exercicio 2.1 e 2.2
        self.arr = []
        self.is_min = is_min
        self.insert_bulk(data)

    # ================ FUNCIONALIDADES "PUBLICAS" ================ 
    # Questao 3.1 
    def insert(self, val):
        self.arr.append(val)
        self._heapify_up(self._get_last_idx())

    # Questão 4.1
    def extract_max(self):
        return self.pop()

    def pop(self):
        if not self.arr:
            return None

        self._troca(0, self._get_last_idx())
        val = self.arr.pop()
        self._heapify_down(0)
        return val

    def peek(self):
        if self.arr:
            return self.arr[0] 
        else :
            return None

    def insert_bulk(self, arr):
        for i in arr:
            self.insert(i)
            # if not self._test():
            #     print(f"Erro ao inserir o elemento : {i}")
            #     return

    # Questão 5.1
    def contains(self, val):
        for i in self.arr:
            if i == val:
                return True
        return False

    # Exercicios 6.1, 6.2 e 6.3
    def delete(self, val):
        idx = self.find(val)
        if idx == -1:
            print(f"Valor ({val}) não existe na heap")
            return

        self._troca(self._get_last_idx(), idx)
        removed = self._get_last_idx()
        last = idx

        if self._has_priority_over(removed, last):
            self._heapify_up(removed )
        if self._has_priority_over(last, removed):
            self._heapify_down(removed )
        self.arr.pop()

    # ================ OVERRIDES ================ 
    def __len__(self):
        return len(self.arr)

    def __str__(self):
        return f"{self.arr}"
    
    # ================ FUNCIONALIDADES INTERNAS ================ 
    def _get_last_idx(self):
        return len(self.arr)-1

    # Para que a Heap possa funcionar tanto como maxima quanto como minima
    # abstraimos o conceito de prioridade
    def _has_priority_over(self, a, b):
        if self.is_min:
            return self.arr[a] < self.arr[b]
        return self.arr[a] > self.arr[b]
    
    # Exercício 2.3
    def _get_left(self, idx):
        return 2*idx+1

    # Exercício 2.3
    def _get_right(self, idx):
        return 2*idx+2

    # Exercício 2.3
    def _get_parent(self, idx):
        return (idx-1)//2
        pass

    def _troca(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    # Exercício 2.4
    def _test(self):
        return self._check(0)
    
    def _check(self, idx):
        last = self._get_last_idx()

        if idx > last: return True
        l = self._get_left(idx)
        r = self._get_right(idx)

        valid_l = l > last or self._has_priority_over(idx, l)
        valid_r = r > last or self._has_priority_over(idx, r)

        return valid_l and valid_r and self._check(l) and self._check(r)

    def _heapify_up(self, start):
        pai_idx = self._get_parent(start)
        if pai_idx >= 0:
            if not self._has_priority_over(pai_idx, start):
                # Exercício 3.2
                # print(f"[HEAPIFY UP] Realizando troca entre os elementos {self.arr[pai_idx]}(idx:{pai_idx}) e {self.arr[start]}(idx:{start})")
                self._troca(pai_idx, start)
                self._heapify_up(pai_idx)

    def _heapify_down(self, start):
        last_idx = self._get_last_idx()
        if start > last_idx:
            return

        l = self._get_left(start)
        r = self._get_right(start)

        # Verifica se o valor l ou r são mais prioritarios que o atual
        troca_l = self._has_priority_over(l, start) if l <= last_idx else False
        troca_r = self._has_priority_over(r, start) if r <= last_idx else False

        # Caso ambos sejam mais prioritarios
        if troca_l and troca_r:
            dir_prioritario = self._has_priority_over(r, l)
            if not dir_prioritario:
                troca_r = False
            else:
                troca_l = False
        
        # Realiza as trocas e propaga
        if troca_l:
            # Exercício 4.2
            #print(f"[HEAPIFY DOWN] Realizando troca entre os elementos {self.arr[start]}(idx:{start}) e {self.arr[l]}(idx:{l})")    
            self._troca(start, l)
            self._heapify_down(l)
        if troca_r:
            # Exercício 4.2
            #print(f"[HEAPIFY DOWN] Realizando troca entre os elementos {self.arr[start]}(idx:{start}) e {self.arr[r]}(idx:{r})")    
            self._troca(start, r)
            self._heapify_down(r)

    def find(self, val):
        for i in range(len(self.arr)):
            if self.arr[i] == val:
                return i
        return -1