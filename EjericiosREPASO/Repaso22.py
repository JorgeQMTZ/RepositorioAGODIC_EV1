def separar(lista):
    lista.sort()
    pares=[]
    impares=[]
    
for n in lista:
    if n%2 == 0:
        pares.append(n)
        else:
            impares.append(n)
            return pares, impares
            pares, impares = separar(numeros)
        
print(pares)
print(impares)