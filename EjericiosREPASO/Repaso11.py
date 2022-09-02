def validarDNI(dni):
    cantidad=0
    while dni!=0:
        cantidad+=1
        dni//=10
    return cantidad==7 or cantidad==8

dni=int(input("Numero DNI: "))

print (validarDNI(dni))