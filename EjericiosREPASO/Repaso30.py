import operator

GUITARRISTAS = [
    {'nombre':'Timo', 'apellido':'Tolski','banda':'Sratovirus'},
    {'nombre':'Eric', 'apellido':'Clapton','banda':'Cream'},
    {'nombre':'Eddie', 'apellido':'Van Halen','banda':'Van Halen'},
    ]

def ordenarXApellido(GUITARRISTAS):
    return sorted(GUITARRISTAS, key=operator.itemgetter('apellido', 'nombre'))

print(ordenarXApellido(GUITARRISTAS))