#Clase principal ó clase padre
class Zoologico:

#Atributos de la clase Zoologico
  def __init__(self , nombre , especie , tipo):

    self.nombre = nombre
    self.especie = especie
    self.tipo = tipo

    self.poblacion = None

#Métodos de la clase Zoologico
  def comer(self):
    print(self.especie , "está comiendo")
  def dormir(self):
    print(self.nombre , "está durmiendo")
  def jugar (self):
    print ("el", self.tipo ,"está jugando")
  def mostrar_poblacion(self):
    self.mostrar_poblacion = numero

#Método traido de la clase premio (Dependencia)
  def premiar(self):
   print(self.nombre , "está siendo premiado")

#Clase de dependencia
class Premio:

#Atributos de la clase Premio (Dependencia)
  def __init__ (self,sabor,tamaño):
    self.sabor = sabor
    self.tamaño = tamaño

#Métodos de la clase Premio (Dependencia)
  def mostrar_sabor(self):
    print ("el premio es" , self.sabor)

#Clase de agregación
class Cliente:

#Atributos de la clase Cliente (Agregación)
  def __init__(self , nombre , edad , sexo):

    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo

#Métodos de la clase Cliente (Agregación)
  def comprar_boleto(self):
    print(self.nombre , "Está comprando")
  def observar_animales(self):
    print(self.nombre , "Está observando")
  def alimentar(self):
    print(self.nombre , "Está alimentando")

#Clase de Herencia
class Empleado (Cliente):
  def __init__(self, nombre, edad, sexo, sueldo):
    super().__init__(nombre, edad, sexo)  

    self.sueldo = sueldo

#Métodos de la clase Empleado (Herencia)
  def trabajar(self):
    print(self.nombre , "Está trabajando")
  def cobrar(self):
    print(self.nombre , "Está cobrando")

#Método heredado de la clase Cliente
  def alimentar(self):
    super().alimentar()
    print (self.nombre , "Está alimentando")

#Clase de asosiación
class Jaulas:

#Atributos de la clase Jaulas (Asociación)
  def __init__(self, id, capacidad, estado):

    self.id = id
    self.capacidad = capacidad
    self.estado = estado

#Métodos de la clase Jaulas (Asociación)
  def mostrar_estado(self):
    print ("La Jaula está lista para usarse")
  def mostrar_capacidad(self):
    print ("La" , self.capacidad ,"tiene animales")
  def mostrar_id(self):
    print ("La jaula" , self.id , "tiene un identificador")

#Clase de composición
class Animales:

#Atributos de la clase Animales (Composición)
  def __init__(self,habitat,alimentacion,poblacion):

    self.habitat = habitat
    self.alimentacion = alimentacion

#Métodos de la clase Animales (Composición)
  def mostrar_habitat(self):
    print("El habitat del animal es: ",self.habitat)
  def mostrar_alimentacion(self):
    print("La alimentacion del animal es: ",self.alimentacion)
  def mostrar_poblacion(self):
    print("La poblacion del animal es: ",self.poblacion)

#Objetos de la clase Zoologico
animal1 = Zoologico("Rayas" , "tigre" , "carnivoro")
animal2 = Zoologico("Pelusa" , "leon" , "carnivoro")
animal3 = Zoologico("Manchas" , "panda" , "herbivoro")

#Objetos de la clase Premio (Dependencia)
premio1 = Premio("dulce" , "pequeño")
premio2 = Premio("salado" , "grande")

#Objetos de la clase Cliente (Agregación)
cliente1 = Cliente("Juan",20,"Masculino")
cliente2 = Cliente("Maria",25,"Femenino")

#Objetos de la clase Empleado (Herencia)
empleado1 = Empleado("Pedro",30,"Masculino",2500)
empleado2 = Empleado ("Fanny", 25 , "Femenino", 2000)

#Objetos de la clase Jaulas (Asociación)
jaula1 = Jaulas(1, "10", "Lista")
jaula2 = Jaulas(2, "15", "No lista")

#Objetos de la clase Animales (Composición)
seres_vivos = Animales("Selva","Carne","Moderada")
seres_vivos2 = Animales("Bosque","Frutas","Controlada")
seres_vivos3 = Animales("Pradera","Frutas","Moderada")

#Mostrar métodos de la clase Zoologico (Agregación)
animal1.dormir()
animal3.dormir()
animal3.jugar()

#Mostrar métodos de la clase Premio (Dependencia)
animal1.premiar()
premio1.mostrar_sabor()

#Mostrar métodos de la clase Empleado (Herencia)
empleado1.trabajar()
empleado2.alimentar()

#Mostrar los métodos de la clase Jaulas (Asociación)
jaula1.mostrar_id()
jaula2.mostrar_estado()

#Mostrar los métodos de la clase Animales (Composición)
seres_vivos.mostrar_habitat()
seres_vivos2.mostrar_alimentacion()

#Prints
print(" ")

print (animal1.nombre, "el" , animal1.especie , "y su amigo" , animal2.nombre , "el" , animal2.especie , "están jugando")

print (" ")

print (animal3.nombre , "el" , animal3.especie) ; animal3.dormir()

print (" ")

print ("El cliente" , cliente1.nombre , "tiene" , cliente1.edad , "años" , "y saldrá en una cita con", cliente2.nombre , "al zoologico a ver a el" , animal1.especie , "y a su amigo el" , animal2.especie)

print (" ")

print (cliente1.nombre , "nota que el" , animal2.especie) ; animal1.dormir()
print (cliente2.nombre , "nota que el" , animal3.especie) ; animal3.jugar()

print(" ")

print (cliente1.nombre, "Observa que la jaula de", animal1.nombre , jaula2.estado, "Por eso", cliente1.nombre, "decide ir a la jaula", jaula1.id, "para ver si hay animales. Después", cliente2.nombre , "Pierde su boleto y lo mira en la jaula", jaula2.id , "en donde está el", animal3.especie)

print(" ")

print (cliente1.nombre , "Vio que el", animal1.especie , "está en la jaula", jaula1.id , "y en la informacion decia que", animal1.nombre, "era" , animal1.tipo , "y que era de la" , seres_vivos.habitat)

print(" ")

