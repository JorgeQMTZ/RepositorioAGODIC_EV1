SEPARADOR = ("*" * 20) + "\n"

cola = list()

for cantidad in range(5):
    nuevo = input("nombre del recien llegado: ")
    cola.append(nuevo)
    
print(f"Se agregaron {len(cola)}, elementos:")
for elementos in cola:
    print(elementos)
print(SEPARADOR)
pass

print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.pop(0))
pass