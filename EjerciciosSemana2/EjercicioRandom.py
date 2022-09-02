import random
SEPARADOR = ("*" * 20) + "\n"

print(f"obteniendo un numero entero aleatorio que puede ir del 0 al 19: {random.randrange(20)}")
print(SEPARADOR)
print(f"obteniendo un numero aleatorio que puede ir deñ 2 al 20: {random.randrange(2, 21, 2)}")
print(SEPARADOR)
print(f"Obteniendo un valor numerico entre 0.0 y 1.0: {random.random()}")
print(SEPARADOR * 2)

listaDePrueba = [10, 20, 30, 40, 15, 25, 35, 45]
print(f"la lista de prueba es {listaDePrueba}")
print(f"el valor seleccionado aleatoriamente de la lista anterior es {random.choice(listaDePrueba)}")
print(SEPARADOR)
random.shuffle(listaDePrueba)
print(f"La lista ya 'perturbada/barajada' es {listaDePrueba}")