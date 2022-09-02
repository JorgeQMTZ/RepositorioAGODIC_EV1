import math
SEPARADOR = ("*" * 20) + "\n"

valorFlotante = float(input("Introduce un numero con fraccion decimal "))
print(f"el siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"el siguiente entero hacia abajo de {valorFlotante} es {math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"La parte entera truncada de {valorFlotante} es {math.trunc(valorFlotante)}")
print(SEPARADOR * 2)
pass

valorNumerico = int(input("Dame un valor entero:\n"))
print(f"La raiz cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"el factorial de {valorNumerico} es igual a {math.factorial(valorNumerico)}")
potencia = int(input("Dame un valor entero:\n"))
print(f"el resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARADOR * 2)
pass
print(f"el valor de pi es {math.pi}")