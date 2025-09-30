class Mascota:
    def __init__(self, nombre="Copito", hambre=10,sueno=10,diversion=10,salud=10,energia=10,felicidad=10,limpieza=10):
        self.nombre = nombre
        self.hambre = hambre
        self.sueno = sueno
        self.diversion = diversion
        self.salud = salud
        self.energia = energia
        self.felicidad = felicidad
        self.limpieza = limpieza

        self.emociones = {
            "super_feliz": r"""
  (\_/)
  ( ^_^)
  / >🍪  Estoy feliz y con energía
""",
            "hambriento": r"""
  (\_/)
  ( ;_;)
  / >🍽️  Tengo hambre
""",
            "cansado": r"""
  (\_/)
  ( -_-) zZ
  / >💤  Tengo sueño
""",
            "muy_cansado": r"""
  (\_/)
  ( -.-)
  / >😴  Muy cansado
""",
            "aburrido": r"""
  (\_/)
  ( -_-)
  / >😐  Aburrido
""",
            "sucio": r"""
  (\_/)
  ( >.<)
  / >💩  Necesito baño
""",
            "enfermo": r"""
  (\_/)
  ( x_x)
  / >💊  Me siento mal
""",
            "triste": r"""
  (\_/)
  ( T_T)
  / >💔  Estoy triste
""",
            "tranquilo": r"""
  (\_/)
  ( ^.^)
  / >🎶  Estoy tranquilo
"""
        }

    def alimentar(self):
        self.hambre -= 7
        self.sueno += 4
        self.felicidad += 1
        print("    ")
        print(f"{self.nombre} HA SIDO ALIMENTADA")

    def dormir(self):
        self.sueno -= 5
        self.energia += 5
        self.salud += 2
        print("    ")
        print(f"{self.nombre} DURMIO UN RATITO")

    def jugar(self):
        self.diversion += 5
        self.felicidad += 3
        self.hambre += 8
        self.energia -= 9
        self.limpieza-=4
        print("    ")
        print(f"JUGASTE CON {self.nombre}.")

    def banar(self):
        self.limpieza += 5
        self.energia -= 5
        self.felicidad += 1
        print("    ")
        print(f"BAÑASTE A {self.nombre}.")

    def ascii_estado(self):
        if self.felicidad > 15 and self.energia > 10:
            return self.emociones["super_feliz"]
        elif self.hambre > 10:
            return self.emociones["hambriento"]
        elif self.sueno > 15:
            return self.emociones["cansado"]
        elif self.energia < 10:
            return self.emociones["muy_cansado"]
        elif self.diversion < 10:
            return self.emociones["aburrido"]
        elif self.limpieza < 10:
            return self.emociones["sucio"]
        elif self.salud < 10:
            return self.emociones["enfermo"]
        elif self.felicidad < 10:
            return self.emociones["triste"]
        else:
            return self.emociones["tranquilo"]

    def mostrar_estado(self):
        print(f"ESTADO GENERAL DE COPITO {self.nombre}:")
        print(f"Hambre: {self.hambre}")
        print(f"Sueño: {self.sueno}")
        print(f"Diversión: {self.diversion}")
        print(f"Salud: {self.salud}")
        print(f"Energía: {self.energia}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Limpieza: {self.limpieza}")
        print(self.ascii_estado())


mi_mascota = Mascota("Copito")

while True:
    print("    ")
    print("BIENVENIDO A TU TAMAGOTCHI")
    print("1) Alimentar")
    print("2) Dormir")
    print("3) Jugar")
    print("4) Bañar")
    print("5) Ver estado")
    print("6) Salir")

    opcion = input("Elige una opción (1-6): ")
    mi_mascota.mostrar_estado()
    if opcion == "1":
        print("    ")
        mi_mascota.alimentar()
    elif opcion == "2":
        print("    ")
        mi_mascota.dormir()
    elif opcion == "3":
        print("    ")
        mi_mascota.jugar()
    elif opcion == "4":
        print("    ")
        mi_mascota.banar()
    elif opcion == "5":
        print("    ")
        mi_mascota.mostrar_estado()
    elif opcion == "6":
        print("    ")
        print("ADIOS, TE EXTRAÑAREEE!!! -COPITO.")
        break
    else:
        print("    ")
        print("Opción inválida, intenta de nuevo.")
