meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Diciembre")
salir = False

while(not salir):
    numero = int(input("Dame un numero apa: " ))
    if(numero==0):
        salir = True
    else:
        if(numero>=1 and numero <=len(meses)):
            print(meses[numero-1])
        else:
            print("Insertame un numero entre 1 y ".len(meses))