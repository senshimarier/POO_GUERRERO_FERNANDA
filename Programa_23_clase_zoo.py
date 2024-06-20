#Programa que contenga una clase, con al menos 3 atributos y 3 metodos, luego cre al menos 2 objetos a partir de la clase y usa algunos de sus atributos y metodos, documenta el codigo
#Commit "Programa 23 - Clases y Objetos"

#Se define el nombre de la clase
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

#Ya con los atributos, clase y metodos definidos, podemos hacer los objetos. Se ponen los datos en el orden en el que van los atributos
animal1= Zoologico("Rayas" , "tigre" , "carnivoro")
animal2= Zoologico("Pelusa" , "leon" , "carnivoro")
animal3= Zoologico("Manchas" , "panda" , "herbivoro")

#Se imprime el nombre del animal, la especie y el tipo de animal, se puede imrpimir metodos, atributos, otros objetos o datos de tipo string que complementen la información
print (animal1.nombre, "el" , animal1.especie , "y su amigo" , animal2.nombre , "el" , animal2.especie , "están jugando, mientras que")

#Por ejemplo en este print, se puede usar el punto y la coma para imprimir por separado los métodos de cada objeto ya que python no permite hacerlo dentro del paréntesis
print (animal3.nombre , "el" , animal3.especie) ; animal3.dormir()
