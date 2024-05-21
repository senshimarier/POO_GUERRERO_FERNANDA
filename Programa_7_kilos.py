print ("Ingrese el peso del paquete")
peso = float(input())

if peso < 1:
  print("Costo de envío: $50")

elif peso <= 5:
  print("Costo de envío: $100")

elif peso <= 10:
  print("Costo de envío: $200")

else:
  print("Costo de envío: $500")
