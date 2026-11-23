
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

    
class ABR:
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
                sx_dx = curn.dupl
                curn.change() #i duplicati della chiave vanno una volta a sinistra e una volta a destra

            if sx_dx == True:
                curn = curn.sx
            else: curn = curn.dx
            
        nuovo.p=curp
        if sx_dx == True:
            curp.sx = nuovo
        else: curp.dx = nuovo

    def delete(self, chiave):
        """Elimina un nodo con la chiave specificata."""
        

if __name__ == "__main__":
    import random
    import libs
    import visualizza

    t = ABR()

    for _ in range(20):
        t.insert(random.randint(0,10))
        

    libs.inorder(t.radice)
    print(libs.altezza(t))
    visualizza.disegna_matplotlib(t)
