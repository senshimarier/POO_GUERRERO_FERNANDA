# Programa que categorice las edades de una lista en grupos
# Infancia (6-11 años), Adolescentes (12-17 años), Jóvenes (18-26 años), Adultos (27 en adelante)

edades = [90, 12, 27, 22, 35, 10, 6, 15, 28, 11] 

infancia = []
adolescentes = []
jovenes = []
adultos = []

for edad in edades:
    if edad >= 6 and edad <= 11:
        infancia.append(edad)

    elif edad >= 12 and edad <= 17:
        adolescentes.append(edad)

    elif edad >= 18 and edad <= 26:
        jovenes.append(edad)

    else:
        adultos.append(edad)

print("Personas en la categoría de Infancia:", infancia)
print("Personas en la categoría de Adolescentes:", adolescentes)
print("Personas en la categoría de Jóvenes:", jovenes)
print("Personas en la categoría de Adultos:", adultos)
    