from Pila_imp import Pila

p = Pila()
print(p.es_vacia())
p.apilar(1)
p.es_vacia()
p.apilar(5)
p.apilar("+")
p.apilar(22)
print(p.mostrarelementos())
print(p.desapilar())
print(p.mostrarelementos())