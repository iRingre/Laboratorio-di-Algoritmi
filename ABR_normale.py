class Nodo:
    def __init__(self, chiave):
        self.chiave = chiave
        self.sx = None
        self.dx = None


class ABR:
    def __init__(self):
        self.radice = None
        self.n = 0  # numero di nodi

    def __len__(self):
        return self.n

    def insert(self, chiave):
        """Inserisce la chiave (anche se gia' presente)."""
        nuovo = Nodo(chiave)
        self.n += 1
        if self.radice is None:
            self.radice = nuovo
            return
        cur = self.radice
        while True:
            if chiave < cur.chiave:
                if cur.sx is None:
                    cur.sx = nuovo
                    return
                cur = cur.sx
            else:  # chiave >= cur.chiave: i duplicati vanno a destra
                if cur.dx is None:
                    cur.dx = nuovo
                    return
                cur = cur.dx

    def search(self, chiave):
        """Restituisce il primo nodo trovato con quella chiave, o None."""
        cur = self.radice
        while cur is not None and cur.chiave != chiave:
            cur = cur.sx if chiave < cur.chiave else cur.dx
        return cur

    def delete(self, chiave):
        """Elimina UNA occorrenza della chiave. Restituisce True se eliminata."""
        parent = None
        cur = self.radice
        while cur is not None and cur.chiave != chiave:
            parent = cur
            cur = cur.sx if chiave < cur.chiave else cur.dx
        if cur is None:
            return False

        # Due figli: si copia la chiave del successore (minimo del
        # sottoalbero destro) e si rimuove fisicamente il successore,
        # che ha al piu' un figlio destro.
        if cur.sx is not None and cur.dx is not None:
            parent_succ = cur
            succ = cur.dx
            while succ.sx is not None:
                parent_succ = succ
                succ = succ.sx
            cur.chiave = succ.chiave
            parent, cur = parent_succ, succ

        figlio = cur.sx if cur.sx is not None else cur.dx
        if parent is None:
            self.radice = figlio
        elif parent.sx is cur:
            parent.sx = figlio
        else:
            parent.dx = figlio
        self.n -= 1
        return True

    def inorder(self):
        """Lista delle chiavi in ordine crescente (duplicati inclusi)."""
        risultato = []
        pila = []
        cur = self.radice
        while pila or cur is not None:
            while cur is not None:
                pila.append(cur)
                cur = cur.sx
            cur = pila.pop()
            risultato.append(cur.chiave)
            cur = cur.dx
        return risultato

    def altezza(self):
        """Numero di nodi del cammino radice-foglia piu' lungo (albero vuoto = 0)."""
        if self.radice is None:
            return 0
        massima = 0
        pila = [(self.radice, 1)]
        while pila:
            nodo, livello = pila.pop()
            if livello > massima:
                massima = livello
            if nodo.sx is not None:
                pila.append((nodo.sx, livello + 1))
            if nodo.dx is not None:
                pila.append((nodo.dx, livello + 1))
        return massima


if __name__ == "__main__":
    import random

    t = ABR()   
    # Test rapido contro una lista ordinata di riferimento
    for _ in range(200):
        t = ABR()
        rif = []
        for _ in range(random.randint(0, 60)):
            k = random.randint(0, 15)  # range piccolo -> molti duplicati
            if random.random() < 0.65:
                t.insert(k)
                rif.append(k)
                rif.sort()
            else:
                eliminato = t.delete(k)
                assert eliminato == (k in rif)
                if eliminato:
                    rif.remove(k)
            assert t.inorder() == rif
            assert len(t) == len(rif)
            assert (t.search(k) is not None) == (k in rif)
    print("Tutti i test passati.")
    print(t.inorder())