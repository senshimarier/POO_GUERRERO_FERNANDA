while True:

  print(" ")
  print("Qué tipo de conversión desea realizar?")

  print("a) Celsius a Fahrenheit")
  print("b) Fahrenheit a Celsius")
  print("c) Salir")

  opcion = input("Ingrese la opción deseada: ")

  print(" ")
  
  if opcion == "a":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grado(s) Celsius equivalen a {fahrenheit} grados Fahrenheit")

  elif opcion == "b":
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} grado(s) Fahrenheit equivalen a {celsius} grados Celsius")
    
  else:
    if opcion == "c":
      print("¡Hasta luego!")
      
      break

  