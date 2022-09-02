def primo(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

numero=int(input("Numero: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")