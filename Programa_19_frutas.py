#Crea un programa con 2 conjuntos con nombres de frutas, luego únelos en un nuevo conjunto y agrega otra fruta. Imprime el resultado de la unión y del conjunto final.
#Commit: Programa 19 – Conjuntos Práctica

c1 = {"manzana", "pera", "fresa"}
c2 = {"banana", "naranja", "mandarina"}

union = c1 | c2
print(union)
print(" ")

union.add("tuna")
print (union)