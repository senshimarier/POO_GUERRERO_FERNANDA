#Crea un programa que una 3 conjuntos, luego recorrer ese conjunto y hacer uno nuevo con únicamente los valores pares, imprimir el resultado.
#Commit: Programa 20 – Conjuntos Números Pares

con1 = {1,2,3}
con3 = {7,8,9}
con2 = {4,5,6}
union = con1 | con2 | con3
for union in con1 | con2 | con3:
  if union % 2 == 0:
    print(union)
