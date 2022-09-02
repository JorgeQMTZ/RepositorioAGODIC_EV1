SEPARADOR = ("*" * 20) + "\n"
lista_vacia = list()
otra_lista_vacia = []
lista_uno = [1,2,3,4]
print(lista_uno)
print(SEPARADOR)
pass

lista_uno.append(5)
print(lista_uno)
lista_uno.append((6,7))
print(lista_uno)
print(SEPARADOR)
pass

lista_uno.remove((6,7))
print(lista_uno)
print(SEPARADOR)
pass

lista_original1 = [3,4,2]
print(lista_original1)
lista_original1.sort()
print(lista_original1)
pass

lista_original2 = [23,10,30, 5]
lista_ordenada = sorted(lista_original2)
print(f"lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")
print(SEPARADOR)
pass

print(f"lista original = {lista_uno}")

lista_uno_al_doble = []
for valor in lista_uno:
    lista_uno_al_doble.append(valor*2)
print(f"Lista resultante, cada elemento al doble = {lista_uno_al_doble}")
pass

lista_uno_al_doble = [valor * 2 for valor in lista_uno]
print(f"Mismo resultado, pero con comprension de listas = {lista_uno_al_doble}")
pass

lista_valores_pares = [valor for valor in lista_uno if(valor% 2==0)]
print(f"Solamente se agregaron los elementos con valor par: {lista_valores_pares}")