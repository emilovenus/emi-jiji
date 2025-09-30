# conceptos_poo.py

# 1. Clases y objetos

#UNA CLASE ES UN PROTOTIPO DEFINIDO POR EL USUARIO PARA UN OBJETO
#QUE DEFINE UN CONJUNTO DE ATRIBUTOS QUE CARACTERIZAN CUALQUIER OBJETO DE LA CLASE
class Persona:
    pass  
#OBJETOS:ENTIDAD QUE CONTIENE AL MISMO TIEMPO UN ESTO (DADO POR LOS VALORES DE LOS ATRIBUTOS)
#Y UN COMPORTAMIENTO (DADO METODOS QUE PERMITEN COMUNICARSE CON DICHO OBJETO)
# Crear objetos (instancias) de la clase Persona
persona1 = Persona()
persona2 = Persona()

# 2. Atributos y métodos
# ATRIBUTO ES LA PROPIEDAD QUE SE LE ASIGNA A UN OBJETO, VARIABLE O ELEMENTO.
# EL METODO PERTENECE A UN OBJETO DE UNA CLASE Y SE UTILIZAN PARA REALIZAR OPERACIONES ESPECIFICAS
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    def saludar(self):        # Método
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# 3. Instancia
# UN OBJETO CREADO A PARTIR DE UNA CLASE
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 25)

# 4. Abstracción
# SIMPLIFICAR MOSTRANDO SOLO LO NECESARIO Y OCULTANDO DETALLES INNECESARIOS
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado.")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")


# 5. Encapsulamiento
# PROTEGR LOS DATOS INTERNS DE UN OBJETO, CONTROLANDO COMO SE ACCEDE O MODIFICA
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio  # Atributo privado

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido.")

# 6. Constructor (__init__)
#METODO ESPECIAL QUE SE EJECUTA AL CREAR UNA INSTANCIA PARA INICIALIZAR ATRIBUTOS
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# 7. Herencia
# PERMITE QUE UNA SUBCLASE HEREDE ATRIBUTOS Y METODOS DE OTRA CLASE
class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra.")

class Gato(Animal):
    def hablar(self):
        print("El gato maúlla.")

# 8. Polimorfismo
# PERMITE QUE UN MISMO METODO TENGA COMPORTSMIENTOS DISTINTOS SWGUN EL OBJETO QUE USE
def hacer_hablar(animal):
    animal.hablar()

# --- Código para probar los ejemplos ---

if __name__ == "__main__":
    # Clases, objetos, atributos y métodos
    persona1.saludar()
    persona2.saludar()

    # Abstracción y encapsulamiento
    cuenta = CuentaBancaria("Carlos", 1000)
    cuenta.mostrar_saldo()
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.mostrar_saldo()

    producto = Producto("Laptop", 1500)
    print(f"Precio inicial: {producto.get_precio()}")
    producto.set_precio(1400)
    print(f"Nuevo precio: {producto.get_precio()}")

    # Herencia y polimorfismo
    perro = Perro()
    gato = Gato()
    hacer_hablar(perro)  # El perro ladra.
    hacer_hablar(gato)   # El gato maúlla.
