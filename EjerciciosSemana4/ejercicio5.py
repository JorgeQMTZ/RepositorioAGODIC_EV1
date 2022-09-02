class Pila:
    def __init__(self):
        self.items = []
        
    def estaVacia(self):
        return self.items==[]
    
    def incluir(self, item):
        self.items.insert(0,item)
        
    def extraer(self):
        return self.items.pop(0)
    
    def inspeccionar(self):
        return self.items[0]
    
    def tamano(self):
        return len(self.items)
    
s = Pila()
s.incluir('hola')
s.incluir('verdadero')

print(s.extraer())