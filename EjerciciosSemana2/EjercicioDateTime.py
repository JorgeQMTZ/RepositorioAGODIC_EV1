import datetime
import time
SEPARADOR = ("*" * 20) + "\n"

hora = datetime.time(10, 20, 30)
print(f"El tipo de objeto de la hora es {type(hora)}")
print(f"La hora es {hora}")
print(f"La hora de {hora} es {hora.hour}") 
print(f"El minuto de {hora} es {hora.minute}") 
print(f"El segundo de {hora} es {hora.second}") 
print(f"El microsegundo de {hora} es {hora.microsecond}") 
print(SEPARADOR * 2)

fecha_actual = datetime.date.today()
print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"La fecha actual es {fecha_actual}")
print(f"El año actual es {fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El día actual es {fecha_actual.day}")
print(SEPARADOR * 2)

fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f"La fecha capturada se transformó a {fecha_procesada}")

cant_dias = int(input("Dime la cantidad de días a adelantar:\n"))
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print(f"La nueva fecha es {nueva_fecha}")
print(SEPARADOR)