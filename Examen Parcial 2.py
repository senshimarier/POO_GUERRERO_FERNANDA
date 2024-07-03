# Clase principal o clase padre
class Zoologico:
    # Atributos de la clase Zoologico
    def __init__(self, nombre, especie, tipo):
        self.nombre = nombre
        self.especie = especie
        self.tipo = tipo
        self.poblacion = None

    # Métodos de la clase Zoologico
    def comer(self):
        print(self.especie, "está comiendo")

    def dormir(self):
        print(self.nombre, "está durmiendo")

    def jugar(self):
        print("El", self.tipo, "está jugando")

    def mostrar_poblacion(self):
        print("La población del zoológico es:", self.poblacion)

    # Método traído de la clase Premio (Dependencia)
    def premiar(self):
        print(self.nombre, "está siendo premiado")


# Clase de dependencia
class Premio:
    # Atributos de la clase Premio (Dependencia)
    def __init__(self, sabor, tamaño):
        self.sabor = sabor
        self.tamaño = tamaño

    # Métodos de la clase Premio (Dependencia)
    def mostrar_sabor(self):
        print("El premio es", self.sabor)


# Clase de agregación
class Cliente:
    # Atributos de la clase Cliente (Agregación)
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    # Métodos de la clase Cliente (Agregación)
    def comprar_boleto(self):
        print(self.nombre, "está comprando un boleto")

    def observar_animales(self):
        print(self.nombre, "está observando a los animales")

    def alimentar(self):
        print(self.nombre, "está alimentando a los animales")


# Clase de herencia
class Empleado(Cliente):
    def __init__(self, nombre, edad, sexo, sueldo):
        super().__init__(nombre, edad, sexo)
        self.sueldo = sueldo

    # Métodos de la clase Empleado (Herencia)
    def trabajar(self):
        print(self.nombre, "está trabajando")

    def cobrar(self):
        print(self.nombre, "está cobrando")

    # Método heredado de la clase Cliente
    def alimentar(self):
        super().alimentar()
        print(self.nombre, "está alimentando a los animales")


# Clase de asociación
class Jaulas:
    # Atributos de la clase Jaulas (Asociación)
    def __init__(self, id, capacidad, estado):
        self.id = id
        self.capacidad = capacidad
        self.estado = estado

    # Métodos de la clase Jaulas (Asociación)
    def mostrar_estado(self):
        print("La jaula está lista para usarse")

    def mostrar_capacidad(self):
        print("La jaula con capacidad de", self.capacidad, "tiene animales")

    def mostrar_id(self):
        print("La jaula", self.id, "tiene un identificador")


# Clase de composición
class Animales:
    # Atributos de la clase Animales (Composición)
    def __init__(self, habitat, alimentacion, poblacion):
        self.habitat = habitat
        self.alimentacion = alimentacion
        self.poblacion = poblacion

    # Métodos de la clase Animales (Composición)
    def mostrar_habitat(self):
        print("El hábitat del animal es:", self.habitat)

    def mostrar_alimentacion(self):
        print("La alimentación del animal es:", self.alimentacion)

    def mostrar_poblacion(self):
        print("La población del animal es:", self.poblacion)

# Clase de asociación
class Tienda:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def mostrar_productos(self):
        print("La tienda", self.nombre, "tiene los siguientes productos:")
        for producto in self.productos:
            print("-", producto)


# Clase de composición
class Habitat:
    def __init__(self, tipo, clima):
        self.tipo = tipo
        self.clima = clima

    def mostrar_info(self):
        print("El hábitat es de tipo", self.tipo, "y su clima es", self.clima)


# Objetos de la clase Zoologico
animal1 = Zoologico("Rayas", "tigre", "carnívoro")
animal2 = Zoologico("Pelusa", "león", "carnívoro")
animal3 = Zoologico("Manchas", "panda", "herbívoro")

# Objetos de la clase Premio (Dependencia)
premio1 = Premio("dulce", "pequeño")
premio2 = Premio("salado", "grande")

# Objetos de la clase Cliente (Agregación)
cliente1 = Cliente("Juan", 20, "Masculino")
cliente2 = Cliente("Maria", 25, "Femenino")

# Objetos de la clase Empleado (Herencia)
empleado1 = Empleado("Pedro", 30, "Masculino", 2500)
empleado2 = Empleado("Fanny", 25, "Femenino", 2000)

# Objetos de la clase Jaulas (Asociación)
jaula1 = Jaulas(1, "10", "Lista")
jaula2 = Jaulas(2, "15", "No lista")

# Objetos de la clase Animales (Composición)
seres_vivos = Animales("Selva", "Carne", "Moderada")
seres_vivos2 = Animales("Bosque", "Frutas", "Controlada")
seres_vivos3 = Animales("Pradera", "Frutas", "Moderada")

# Objetos de la clase Tienda (Asociación)
tienda1 = Tienda("Entrance Zoo", ["Peluches", "Ropa", "Comida"])
tienda2 = Tienda("Exit Zoo", ["Postales", "Juguetes", "Libros"])

# Objetos de la clase Habitat (Composición)
habitat1 = Habitat("Desierto", "Seco")
habitat2 = Habitat("Selva", "Húmedo")

# Función del menú interactivo
def menu():
    while True:
        print("\nEscoge que información quieres ver:")
        print("1. Estado de las jaulas")
        print("2. Alimentar animales (Empleado)")
        print("3. Comprar boleto (Cliente)")
        print("4. Ver premios")
        print("5. Productos de las tiendas")
        print("6. Información de hábitat")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            jaula1.mostrar_estado()
            jaula2.mostrar_estado()
        elif opcion == '2':
            empleado1.alimentar()
            empleado2.alimentar()
        elif opcion == '3':
            cliente1.comprar_boleto()
            cliente2.comprar_boleto()
        elif opcion == '4':
            premio1.mostrar_sabor()
            premio2.mostrar_sabor()
        elif opcion == '5':
            tienda1.mostrar_productos()
            tienda2.mostrar_productos()
        elif opcion == '6':
            habitat1.mostrar_info()
            habitat2.mostrar_info()
        elif opcion == '7':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú interactivo
menu()