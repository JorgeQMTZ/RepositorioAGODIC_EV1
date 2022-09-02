class persona:
    def __init__ (self, nombre, apellido, n_alumno):
        self.nombre = nombre
        self.apellido = apellido
        self.n_alumno = n_alumno
        self.notas = []
        
juan = persona ('Juan', 'Aguila', '14000000')
aldo = persona ('Aldo', 'Verri', '14000001')
maria = persona ('Maria', 'Pinto', '14000002')

juan.notas.extend ([6.5, 7.0, 6.7])
aldo.notas.extend ([3.0, 2.7, 3.8])
maria.notas.extend ([5.7, 7.0, 6.2])

estudiantes = [juan, aldo, maria]

for e in estudiantes:
    promedio = sum (e.notas)/len(e.notas)
    print (e.apellido,"\t= >",'%0.2 f%', promedio)