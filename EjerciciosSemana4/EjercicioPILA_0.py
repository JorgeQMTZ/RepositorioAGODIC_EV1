class Pila:
    
    def __init__(self):
        self.items=[]
        
    def apilar(self, x):
        self.items.append(x)
        
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
        
    def es_vacia(self):
        return self.items == []
    
    def mostrarelementos(self):
        print ("Los elementos de la pila son: ")
        print (self.items)