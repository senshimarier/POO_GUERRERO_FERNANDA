#Programa que simule una calculadora básica al permitir al usuario seleccionar la opción de sumar, restar, multiplicar o dividir dos números ingresados llamando una función por cada operación.
#Commit “Programa 22 –Calculadora Básica con Funciones” 

print ("Ingrese dos números y después seleccione la operación que desea realizar:")

print ("Número 1:")
a = float(input())
print(" ")
print ("Número 2:")
b = float(input())

operacion = input("\na) Suma \nb) Resta \nc) Multiplicacion \nd) División: ")

if operacion == "a":
  def suma(a,b):
    return a+b
  print ("El resultado de la suma es:", suma(a,b))

elif operacion == "b":
  def resta(a,b):
    return a-b
  print ("El resultado de la resta es:", resta(a,b))

elif operacion == "c":
  def multiplicación(a,b):
    return a*b
  print ("El resultado de la multiplicación es: ", multiplicación(a,b))

elif operacion == "d":
  def división(a,b):
    return a//b
  print ("El resultado de la división es:", división(a,b))

else:
  print ("Syntax Error")