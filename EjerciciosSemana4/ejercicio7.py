'''
Demostración de implementación de pilas utilizando deques
'''
import collections
SEPARADOR = ("*" * 20) + "\n"

pila_deque = collections.deque()
for i in range(5):
    pila_deque.append(input("Dime el nombre a agregar: "))


while pila_deque:
    print(pila_deque.pop())
pass
