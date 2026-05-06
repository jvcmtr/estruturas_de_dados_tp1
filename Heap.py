

class Heap:
    def __init__(self, data = [], is_min=True):
        self.arr = []
        self.is_min = is_min
        self.insert_bulk(data)

    def insert(self, val):
        self.arr.append(val)
        self._heapify_up(self._get_last_idx())

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

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        return f"{self.arr}"
    
    def _get_last_idx(self):
        return len(self.arr)-1

    def _has_priority_over(self, a, b):
        if self.is_min:
            return self.arr[a] < self.arr[b]
        return self.arr[a] > self.arr[b]
    
    def _get_left(self, idx):
        return 2*idx+1

    def _get_right(self, idx):
        return 2*idx+2
        pass

    def _get_parent(self, idx):
        return (idx-1)//2
        pass

    def _troca(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def _test(self):
        return self._check(0)
    
    def _check(self, idx):
        if idx > self._get_last_idx():
            return True
        l = self._get_left(idx)
        r = self._get_right(idx)
        valid_l = self._has_priority_over(idx, l) if l <= self._get_last_idx() else True
        valid_r = self._has_priority_over(idx, r) if r <= self._get_last_idx() else True
        ok = valid_l and valid_r and self._check(l) and self._check(r)
        if not ok:
            print(f"Atual (id:{idx}) mais prioritario que l (id:{l}) : {valid_l}")
            print(f"Atual (id:{idx}) mais prioritario que r (id:{r}) : {valid_r}")
        return ok

    def _heapify_up(self, start):
        pai_idx = self._get_parent(start)
        if pai_idx >= 0:
            if not self._has_priority_over(pai_idx, start):
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
            self._troca(start, l)
            self._heapify_down(l)
        if troca_r:
            self._troca(start, r)
            self._heapify_down(r)

