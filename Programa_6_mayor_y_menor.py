print ("Ingresa un número")
número1 = float(input())

print ("Ingresa otro número")
número2 = float(input())

if número1 > número2:
  print ("El número mayor es:" , número1)
  print ("El número menor es" , número2)

elif número1 < número2:

  print ("El número mayor es" , número2)
  print ("El número menor es" , número1)

else:
  print ("Ambos números son iguales")