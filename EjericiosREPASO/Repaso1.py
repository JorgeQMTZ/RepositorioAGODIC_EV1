def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
        return False
    
direccion=input("Tu email: ")
if validar(direccion):
    print("Valido")
else:
    print("Invalido")