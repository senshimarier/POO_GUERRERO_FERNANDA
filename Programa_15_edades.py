
listas = [12,90,50,22,35,10,6,15,28,11] 

listamenor = []
listamayor = []

for lista in listas:
    if lista >= 18:
        listamayor.append(lista)
    else:
        listamenor.append(lista)

print("La persona es menor de edad", listamenor)
print("La persona es mayor de edad", listamayor)
