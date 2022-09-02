diccionario_vacio = {}
diccionario_citas = {"T'Challa":"Wakanda Forever",
            "Thanos":"The hardest choices require the strongest wills",
            "AMLO":"Me canso ganso"}

print(diccionario_citas)
pass

print(diccionario_citas["Thanos"])
pass

print("*" * 20)
diccionario_citas["Plankton"] = "¡Por fin tengo la fórmula de la cangreburger"
print(diccionario_citas)
pass

print("*" * 20)
del diccionario_citas["AMLO"]
print(diccionario_citas)
pass

print(list(diccionario_citas.keys()))
pass

print(list(diccionario_citas.values()))
pass

print(list(diccionario_citas.items()))