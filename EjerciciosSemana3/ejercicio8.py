class Cola:
    
    def __init__(self):
        self.datos=[]
        
    def cantidad(self):
        return len(self.datos)
    
    def insertar(self, dato):
        self.datos.insert(0,dato)
        
    def extraer(self):
        if self.cantidad():
            return self.datos.pop()
        else:
            return None
        
    def primer_dato(self):
        if self.cantidad():
            return self.datos[-1]
        
    def ultimo_dato(self):
        if self.cantidad():
            return self.datos[0]
        
numeros = Cola()
numeros.insertar(2)
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)

print(numeros.primer_dato())
print(numeros.ultimo_dato())
print(numeros.cantidad())

print()

dato = numeros.extraer()
print(dato)
print(numeros.cantidad())

print()

numeros.extraer()
numeros.extraer()
numeros.extraer()
print(numeros.cantidad())

print()

dato=numeros.extraer()
print(dato)