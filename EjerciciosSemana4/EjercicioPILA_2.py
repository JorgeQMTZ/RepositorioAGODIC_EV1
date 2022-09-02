from Pila_imp import Pila

p=Pila()

print(p.es_vacia())
p.apilar(4)
p.apilar('perro')
print(p.inspeccionar())
p.apilar(True)
print(p.tamano())
print(p.es_vacia())
p.apilar(8.4)
print(p.mostrarelementos())
print(p.desapilar())
print(p.desapilar())
print(p.tamano())
print(p.mostrarelementos())
