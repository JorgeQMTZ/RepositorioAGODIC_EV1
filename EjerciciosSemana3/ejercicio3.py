cola = []

def main():
    print("1 - insertar cola")
    print("2 - borrar cola")
    print("3 - listar cola")
    print("4 - salir")
    
    option = input("elije una opcion: ")
    
    if str(option)=="1":
        elemento = input("introduzca el numero a encolar: ")
        cola.append(elemento)
        print("numero encolado con exito")
        main()
        
    elif str(option)=="2":
        if len(cola)>0:
            print("el numero: ",cola.pop(0),"fue desencolado")
            main()
        else:
            print("cola vacia")
            main()
                
    elif str(option)=="3":
        for i in cola:
            print("cola:",i)
        main()
        
        
    elif str(option)=="4":
        exit()
    else:
        print("seleccione una opcion valida.")
        
main()