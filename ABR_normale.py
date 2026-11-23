class Nodo:
    def __init__(self, chiave):
        self.chiave = chiave
        self.sx = None
        self.dx = None
        self.p = None


class ABR:
    def __init__(self):
        self.radice = None
        self.n = 0 


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

    def delete(self, chiave):
        """Elimina UNA occorrenza della chiave. Restituisce True se eliminata."""
        parent = None
        cur = self.radice
        while cur is not None and cur.chiave != chiave:
            parent = cur
            cur = cur.sx if chiave < cur.chiave else cur.dx

        if cur is None:
            return False

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


if __name__ == "__main__":
        import random
        import libs
        import visualizza

        t = ABR()

        for _ in range(20):
            t.insert(random.randint(0,5))

        print(libs.altezza(t))
        visualizza.disegna_matplotlib(t)