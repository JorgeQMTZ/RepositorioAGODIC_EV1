import random
SEPARADOR = ("*" * 20) + "\n"

lista = [random.randrange(1,101) for valor in range(10)]
print(type(lista))
print(f"El primer elemento es {lista[0]} y el último es {lista[9]}")
print(type(lista))
print(SEPARADOR)

lista_de_listas = [[random.randrange(1,101) for valor in range(10)] for valor in range(5)]
print(lista_de_listas)
print(f"El primer elemento es {lista_de_listas[0][0]} y el último es {lista_de_listas[4][9]}")
print(lista_de_listas[0])
for lista_interna in lista_de_listas:
    print(lista_interna[0])
    

print(type(lista_de_listas))

print("[")
for lista_primer_nivel in lista_de_listas:
    print(f"lista interna: {lista_primer_nivel}")
    print("[", end="")
    for elemento in lista_primer_nivel:
        print(f"{elemento}", end="\t")
    print("]", end="")
    print("")
    
print("]")
print(SEPARADOR)

print(f"El elemento 0,2 es {lista_de_listas[0][2]}")
print(f"El elemento 2,7 es {lista_de_listas[2][7]}")