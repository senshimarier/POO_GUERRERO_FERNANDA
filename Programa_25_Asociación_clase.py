#Commit - Programa 25 - clases y objetos - Asociacion


#Se define otra clase para el commit 25
class Jaulas:
  def __init__(self, id, capacidad, estado):

#Se definen los atributos de la clase
    self.id = id
    self.capacidad = capacidad
    self.estado = estado
  

#Se definen los metodos
def estado(self):
  print ("La jaula está/no está lista para usarse")
def capacidad(self):
  print ("La jaula tiene/no tiene animales")
def id(self):
  print ("La jaula ya tiene un identificador")


#Se crean objetos de la clase Jaulas
jaula1 = Jaulas(1, "10", "Lista")
jaula2 = Jaulas(2, "15", "No lista")


  #Hay algunos prints de la nueva clase junto con las otras, abajo :)#

class Zoologico:

  #Se definen los atributos de la clase
  def __init__(self , nombre , especie , tipo):

    #Aqui se le agrega un punto para luego jalarlo y también se definen
    self.nombre = nombre
    self.especie = especie
    self.tipo = tipo

#Aqui se definen los métodos/funciones de la clase, lo que el animal puede hacer
  def comer(self):
    print("Está comiendo")
  def dormir(self):
    print("Está durmiendo")
  def jugar (self):
    print ("Está jugando")
#/////////Aqui empieza el programa 24///////////
#Aqui se crea otra clase, con al menos 3 atributos y 3 métodos
class Cliente:
  #Se definen los atributos de la clase
  def __init__(self , nombre , edad , sexo):

    #Aqui se le agrega un punto para luego jalarlo y definirlo
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo

#Aqui se definen los métodos/funciones de la clase, lo que el cliente puede hacer
  def comprar_boleto(self):
    print("Está comprando")
  def observar_animales(self):
    print("Está observando")
  def alimentar(self):
    print("Está alimentando")
#Definimos los objetos dentro de la clase y ordenamos segun la informacion
cliente1=Cliente("Juan",20,"Masculino")
cliente2=Cliente("Maria",25,"Femenino")


#/////////Aqui termina el programa 24///////////

#Ya con los atributos, clase y metodos definidos, podemos hacer los objetos. Se ponen los datos en el orden en el que van los atributos
animal1= Zoologico("Rayas" , "tigre" , "carnivoro")
animal2= Zoologico("Pelusa" , "leon" , "carnivoro")
animal3= Zoologico("Manchas" , "panda" , "herbivoro")

#Se imprime el nombre del animal, la especie y el tipo de animal, se puede imrpimir metodos, atributos, otros objetos o datos de tipo string que complementen la información
print (animal1.nombre, "el" , animal1.especie , "y su amigo" , animal2.nombre , "el" , animal2.especie , "están jugando, mientras que")

#Por ejemplo en este print, se puede usar el punto y la coma para imprimir por separado los métodos de cada objeto ya que python no permite hacerlo dentro del paréntesis
print (animal3.nombre , "el" , animal3.especie) ; animal3.dormir()

#Este es un print del programa 24, con la clase zoologico y la clase cliente en conjunto
print ("El cliente" , cliente1.nombre , "tiene" , cliente1.edad , "años" , "y saldrá en una cita con", cliente2.nombre , "al zoologico a ver a el" , animal1.especie , "y a su amigo el" , animal2.especie)

print (cliente1.nombre , "nota que el" , animal2.especie) ; animal1.dormir()
print (cliente2.nombre , "nota que el" , animal3.especie) ; animal3.jugar()

#Print de todos los objetos creados
print (cliente1.nombre, "Observa que la jaula de", animal1.nombre , jaula2.estado, "Por eso", cliente1.nombre, "decide ir a la jaula", jaula1.id, "para ver si hay animales. Después", cliente2.nombre , "Pierde su boleto y lo mira en la jaula", jaula2.id , "en donde está el", animal3.especie)

