def linearSearch(item, my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
        
    return found

bag = ['libro', 'lapiz', 'pluma', 'marcador', 'regla']
item = input("Que articulo buscas pa? ")
itemFound = linearSearch(item,bag)
if itemFound:
    print("Si esta pa")
else:
    print("NO esta pa, te lo ratiaste")