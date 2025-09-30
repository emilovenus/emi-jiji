from random import randint as rd
class Persona:
    def __init__(self, nombre, edad, genero, altura, profesion):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.profesion = profesion

    # Métodos
    def presentarse(self):
        print( f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        print(f"------------------------------------------------")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Soy {self.nombre} y Cumpli {self.edad}!!!!")
        print(f"------------------------------------------------")
    
    def describir(self):
        print(f"Soy {self.nombre}, Tengo {self.edad} años, Soy {self.genero}, mido {self.altura} cm y soy {self.profesion}.")
        print(f"------------------------------------------------")

    def cambiagenero(self):
        if self.genero=="Mujer":
            self.genero="Hombre"
        elif self.genero=="Hombre":
            self.genero="Mujer"
        else:
            self.genero="TLACUACHE"
        print(f"{self.nombre} ha cambiado de genero a {self.genero}")
        print(f"------------------------------------------------")

    def crecer(self):
        self.altura=self.altura+rd(0,100)
        print(f"{self.nombre} crecio y ahora mide {self.altura}")
        print(f"------------------------------------------------")



pers1 = Persona("Emily", 19, "Mujer", 169, "Estudiante" )
pers2 = Persona("Fabian", 24, "Hombre", 170, "Estudiante" )
pers3 = Persona("Martin", 24, "Hombre", 186, "Biologo" )
pers4 = Persona("Bryant", 26, "Hombre", 173, "Subgerente" )

print(f"************************* ")
print(f"EMILY: ")
print(f" ")
pers1.presentarse()
pers1.cumplir_anios()
print(f"************************* ")
print(f"FABIAN: ")
print(f" ")
pers2.cambiagenero()
pers2.crecer()
print(f"************************* ")
print(f"MARTIN: ")
print(f" ")
pers3.describir()
print(f"************************* ")
print(f"BRYANT: ")
print(f" ")
pers4.cumplir_anios()
pers4.describir()
    


