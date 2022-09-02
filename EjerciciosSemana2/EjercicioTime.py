import time
SEPARADOR = ("*" * 20) + "\n"

segundos = int(input("cantidad de segundos a esperar:\n"))
time.sleep(segundos)
print(f"Han transcurrido, por lo menos, {segundos} segudnos")
print(SEPARADOR * 2)

print("iniciaremos la medicion de un proceso simulado")

horaInicial = time.time()

for termino in range(10):
    time.sleep(segundos)
    
print("proceso simulado concluido")
duracion = time.time() - horaInicial
print(f"La duracion del proceso simulado fue de {duracion} segudnos")