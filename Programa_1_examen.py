#Programa que pida al usuario un número e identificar si es positivo, negativo o cero.
print("Ingresa un número:")
numero = float(input())

if numero > 0:
  print("El numero es positivo" , numero)
  
elif numero < 0:
  print ("El numero es negativo" , numero)
  
elif numero == 0:
  print ("El numero es cero" , numero)
  
else:
  print("El numero no es valido")