#Iterar sobre un diccionario
Oxxo = {
  "Maruchan:": 21,
  "Coca-cola:": 25,
  "Jabón Zote:": 40,
  "Cheetos:": 17,
  "Café:" : 30,
}

descuento = 0.10

for producto, precio in Oxxo.items():
  print(producto, precio)
  
  print("Precio con descuento: ", precio and (precio * descuento))
  

