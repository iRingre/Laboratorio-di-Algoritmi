def inorder(root):
    """Stampa in ordine crescente di tutte le chiavi di un albero"""
    if root is None: return

    inorder(root.sx)
    print(root.chiave)
    inorder(root.dx)

def preorder(root):
    """Stampa in ordine anticipato di tutte le chiavi di un albero"""
    if root is None: return

    print(root.chiave)
    preorder(root.sx)
    preorder(root.dx)

def postorder(root):
    """Stampa in ordine posticipato di tutte le chiavi di un albero"""
    if root is None: return
    postorder(root.sx)
    postorder(root.dx)
    print(root.chiave)

def trapianta(t, u, v):
    """Sostituisce il sottoalbero con radice u con quello con radice v."""
    if u.p is None:
        t.radice = v
    elif u is u.p.sx:
        u.p.sx = v
    else:
        u.p.dx = v
    if v is not None:
        v.p = u.p

def minimo(x):
    """Nodo con chiave minima nel sottoalbero di x."""
    while x.sx is not None:
        x = x.sx
    return x

def massimo(x):
    """Nodo con chiave massima nel sottoalbero di x."""
    while x.dx is not None:
        x = x.dx
    return x

def successore(x):
    if x.dx is not None:
        return minimo(x.dx)
    y = x.p
    while y is not None and x is y.dx:
        x = y
        y = y.p
    return y

def predecessore(x):
    if x.sx is not None:
        return massimo(x.sx)
    y = x.p
    while y is not None and x is y.sx:
        x = y
        y = y.p
    return y


def altezza(t):
    """Numero di nodi del cammino radice-foglia piu' lungo (albero vuoto = 0)."""
    if t.radice is None:
        return 0
    massima = 0
    pila = [(t.radice, 1)]
    while pila:
        nodo, livello = pila.pop()
        if livello > massima:
            massima = livello
        if nodo.sx is not None:
            pila.append((nodo.sx, livello + 1))
        if nodo.dx is not None:
            pila.append((nodo.dx, livello + 1))
    return massima

def search(t, chiave):
    """Restituisce il primo nodo trovato con quella chiave, o None."""
    cur = t.radice
    while cur is not None and cur.chiave != chiave:
        cur = cur.sx if chiave < cur.chiave else cur.dx
    return cur