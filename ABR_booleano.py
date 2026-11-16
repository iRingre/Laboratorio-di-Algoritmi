def inorder(root):
    """Lista delle chiavi in ordine crescente (duplicati inclusi)."""
    if root is None: return

    inorder(root.sx)
    print(root.chiave)
    inorder(root.dx)

def preorder(root):
    if root is None: return

    print(root.chiave)
    preorder(root.sx)
    preorder(root.dx)

def postorder(root):
    if root is None: return
   
    postorder(root.sx)
    postorder(root.dx)
    print(root.chiave)



class Node:
    def __init__(self, chiave):
        self.chiave = chiave
        self.sx = None
        self.dx = None
        self.p = None
        self.dupl = False

    def change(self):
            if self.dupl == False:
                self.dupl = True
            else: self.dupl = False

    
class ABRbool:
    def __init__(self):
        self.radice = None
        self.n = 0

    def insert(self, chiave):
        """Inserisce un nuovo nodo con chiave e se la chiave è gia presente la inserisce in base ad un flag booleano"""
        nuovo = Node(chiave)
        curn = self.radice
        curp = None
        self.n +=1
        sx_dx = False
        if self.radice == None:
            self.radice = nuovo
            return
        
        while curn != None:
            curp = curn
            
            if nuovo.chiave < curn.chiave:
                sx_dx = True
            elif nuovo.chiave > curn.chiave: 
                sx_dx = False
            else:
                curn.change()
                sx_dx = curn.dupl

            if sx_dx == True:
                curn = curn.sx
            else: curn = curn.dx
            
        nuovo.p=curp
        if sx_dx == True:
            curp.sx = nuovo
        else: curp.dx = nuovo

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

    t = ABRbool()

    for _ in range(30):
        t.insert(random.randint(0,5))

    inorder(t.radice)
    print(t.altezza())
