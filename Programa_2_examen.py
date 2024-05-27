#Programa que pregunte al usuario que área quiere cálcular(cuadrado, triángulo o recttángulo) y que repita el proceso hasta que el usuario escriba "salir"

#Programa que se hizo en la clase de Aviña jeje ;)

def area():
  figura = input(
      "¿De qué figura desea calcular el área? \na)rectángulo \nb)cuadrado \nc)triángulo: "
  )
  match figura:
      case "rectángulo":
          base = float(input("Ingresa la base del rectángulo: "))
          altura = float(input("Ingresa la altura del rectángulo: "))
          area = base * altura // 2
          print("El área del círculo es:", area)

      case "cuadrado":
          lado = float(input("Ingresa la medida del lado del cuadrado: "))
          area = lado**2
          print("El área del cuadrado es:", area)

      case "triángulo":
          base = float(input("Ingresa la medida de la base del triángulo: "))
          altura = float(
              input("Ingresa la medida de la altura del triángulo: "))
          area = (base * altura) / 2
          print("El área del triángulo es:", area)

      case "a":
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura // 2
        print("El área del círculo es:", area)

      case "b":
          lado = float(input("Ingresa la medida del lado del cuadrado: "))
          area = lado**2
          print("El área del cuadrado es:", area)

      case "c":
          base = float(input("Ingresa la medida de la base del triángulo: "))
          altura = float(
              input("Ingresa la medida de la altura del triángulo: "))
          area = (base * altura) / 2
          print("El área del triángulo es:", area)

      case _:
          print("Figura no válida.")



while True:
  area()
  respuesta = input("¿Desea calcular el área de otra figura? (s/n)")
  if respuesta == "n" or respuesta == "no":
      break