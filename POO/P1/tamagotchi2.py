class Mascota:
    def __init__(self, nombre="Copito", hambre=10, sueno=10, diversion=10, salud=10, energia=10, felicidad=10, limpieza=10):
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
  / >🍪  ¡Estoy super feliz y lleno de energía!
""",
            "hambriento": r"""
  (\_/)
  ( ;_;)
  / >🍽️  Tengo mucha hambre...
""",
            "cansado": r"""
  (\_/)
  ( -_-) zZ
  / >💤  Tengo demasiado sueño...
""",
            "muy_cansado": r"""
  (\_/)
  ( -.-)
  / >😴  Estoy muy cansado...
""",
            "aburrido": r"""
  (\_/)
  ( -_-)
  / >😐  Estoy aburrido...
""",
            "sucio": r"""
  (\_/)
  ( >.<)
  / >💩  ¡Necesito un baño!
""",
            "enfermo": r"""
  (\_/)
  ( x_x)
  / >💊  Me siento enfermo...
""",
            "triste": r"""
  (\_/)
  ( T_T)
  / >💔  Estoy triste...
""",
            "tranquilo": r"""
  (\_/)
  ( ^.^)
  / >🎶  Estoy tranquilo.
"""
        }


    def alimentar(self):
        self.hambre -= 5
        self.sueno += 2
        self.felicidad += 1
        print(f"Alimentaste a {self.nombre}.")

    def dormir(self):
        self.sueno -= 5
        self.energia += 5
        self.salud += 2
        print(f"{self.nombre} durmió un rato.")

    def jugar(self):
        self.diversion += 5
        self.felicidad += 3
        self.hambre += 3
        self.energia -= 2
        print(f"Jugaste con {self.nombre}.")

    def banar(self):
        self.limpieza += 5
        self.energia -= 1
        self.felicidad += 1
        print(f"Bañaste a {self.nombre}.")


    def ascii_estado(self):
        if self.felicidad > 15 and self.energia > 10:
            return self.emociones["super_feliz"]
        elif self.hambre > 15:
            return self.emociones["hambriento"]
        elif self.sueno > 15:
            return self.emociones["cansado"]
        elif self.energia < 5:
            return self.emociones["muy_cansado"]
        elif self.diversion < 5:
            return self.emociones["aburrido"]
        elif self.limpieza < 5:
            return self.emociones["sucio"]
        elif self.salud < 5:
            return self.emociones["enfermo"]
        elif self.felicidad < 5:
            return self.emociones["triste"]
        else:
            return self.emociones["tranquilo"]

    def estado(self):
        return (f"\nEstado de {self.nombre}:\n"
                f"Hambre: {self.hambre}\n"
                f"Sueño: {self.sueno}\n"
                f"Diversión: {self.diversion}\n"
                f"Salud: {self.salud}\n"
                f"Energía: {self.energia}\n"
                f"Felicidad: {self.felicidad}\n"
                f"Limpieza: {self.limpieza}\n"
                f"{self.ascii_estado()}"
                )


mi_mascota = Mascota("Copito")

while True:
    print("\n¿Qué quieres hacer con tu Tamagotchi?")
    print("1. Alimentar")
    print("2. Dormir")
    print("3. Jugar")
    print("4. Bañar")
    print("6. Salir")

    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        mi_mascota.alimentar()
    elif opcion == "2":
        mi_mascota.dormir()
    elif opcion == "3":
        mi_mascota.jugar()
    elif opcion == "4":
        mi_mascota.banar()
    elif opcion == "5":
        print(mi_mascota.estado())
        continue
    elif opcion == "6":
        print("¡Adiós! Gracias por jugar con tu Tamagotchi.")
        break
    else:
        print("Número inválido, intenta de nuevo.")
        continue

    print(mi_mascota.estado())
