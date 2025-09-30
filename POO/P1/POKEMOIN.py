import os
import pickle
import random

# =========================
# CLASES BASE
# =========================
class Movimiento:
    def __init__(self, nombre, poder, tipo):
        self.nombre = nombre
        self.poder = poder
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} (Poder: {self.poder}, Tipo: {self.tipo})"

class Pokemon:
    def __init__(self, nombre, tipo, hp, movimientos, arte_ascii):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.hp_max = hp
        self.movimientos = movimientos
        self.arte_ascii = arte_ascii

    def atacar(self, movimiento, objetivo):
        print(f"\n{self.nombre} usa {movimiento.nombre} contra {objetivo.nombre}!")
        objetivo.hp -= movimiento.poder
        if objetivo.hp < 0:
            objetivo.hp = 0

    def mostrar_estado(self):
        print(f"\n{self.nombre} ({self.tipo}) - HP: {self.hp}/{self.hp_max}")
        print(self.arte_ascii)

# =========================
# CLASE JUGADOR
# =========================
class Jugador:
    def __init__(self, nombre, pokemon):
        self.nombre = nombre
        self.pokemon = pokemon
        self.x = 5
        self.y = 5

# =========================
# CLASE MAPA
# =========================
class Mapa:
    def __init__(self, ancho=10, alto=10):
        self.ancho = ancho
        self.alto = alto
        self.pokemon_salvajes = []

    def generar_pokemon_salvaje(self):
        """Genera un Pokémon salvaje en una posición aleatoria"""
        garfang = Pokemon("Garfang", "Bestia", 40,
            [
                Movimiento("Arañazo Feroz", 8, "Bestia"),
                Movimiento("Mordida", 10, "Bestia"),
                Movimiento("Garra Oscura", 12, "Sombra"),
                Movimiento("Zarpazo Final", 15, "Bestia")
            ],
            r"""
            /\_/\  
           ( o.o )≡
            > ^ <
            """)
        aquary = Pokemon("Aquary", "Agua", 45,
            [
                Movimiento("Chorro Helado", 7, "Agua"),
                Movimiento("Burbuja Golpe", 9, "Agua"),
                Movimiento("Ola Impacto", 11, "Agua"),
                Movimiento("Tsunami", 14, "Agua")
            ],
            r"""
            ><(((º>  
            """)

        opciones = [garfang, aquary]
        poke = random.choice(opciones)
        x = random.randint(0, self.ancho - 1)
        y = random.randint(0, self.alto - 1)

        self.pokemon_salvajes.append((poke, x, y))

    def dibujar(self, jugador):
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                if x == jugador.x and y == jugador.y:
                    fila += "😀 "  # Jugador
                elif any(px == x and py == y for _, px, py in self.pokemon_salvajes):
                    fila += "👾 "  # Pokémon salvaje
                else:
                    fila += ". "
            print(fila)
        print("\nUsa WASD para moverte, M para menú, Q para salir.")

# =========================
# FUNCIONES DE GUARDADO
# =========================
def guardar_partida(jugador):
    with open(f"{jugador.nombre}.dat", "wb") as f:
        pickle.dump(jugador, f)
    print("✅ Partida guardada.")

def cargar_partida(nombre):
    try:
        with open(f"{nombre}.dat", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("❌ No existe una partida con ese nombre.")
        return None

def borrar_partida(nombre):
    try:
        os.remove(f"{nombre}.dat")
        print(f"🗑️ Partida {nombre} borrada.")
    except FileNotFoundError:
        print("❌ No existe esa partida.")

# =========================
# MENU PRINCIPAL
# =========================
def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Crear Partida")
        print("2. Continuar Partida")
        print("3. Borrar Partida")
        print("4. Salir")
        opcion = input("> ")

        if opcion == "1":
            crear_partida()
        elif opcion == "2":
            nombre = input("Nombre del jugador: ")
            jugador = cargar_partida(nombre)
            if jugador:
                jugar(jugador)
        elif opcion == "3":
            nombre = input("Nombre de la partida a borrar: ")
            borrar_partida(nombre)
        elif opcion == "4":
            break

# =========================
# CREAR PARTIDA
# =========================
def crear_partida():
    nombre = input("Escribe tu nombre: ")

    # Movimientos iniciales
    golpe = Movimiento("Golpe Sombrío", 10, "Sombra")
    garra = Movimiento("Garra Maldita", 12, "Sombra")
    rayo = Movimiento("Rayo Solar", 12, "Luz")
    luz_corte = Movimiento("Corte Lumínico", 14, "Luz")

    # Pokemones iniciales
    sombrachu = Pokemon("Sombrachu", "Sombra", 55, [golpe, garra], 
        r"""
        (\__/)
        (●_● )
        />🌑 
        """)
    
    luminix = Pokemon("Luminix", "Luz", 55, [rayo, luz_corte],
        r"""
        /\_/\  
       ( o.o )✨
        > ^ < 
        """)

    print("\nElige tu compañero:")
    print("1.", sombrachu.nombre)
    print(sombrachu.arte_ascii)
    print("2.", luminix.nombre)
    print(luminix.arte_ascii)

    eleccion = input("> ")
    if eleccion == "1":
        pokemon = sombrachu
    else:
        pokemon = luminix

    jugador = Jugador(nombre, pokemon)
    guardar_partida(jugador)
    jugar(jugador)

# =========================
# COMBATE
# =========================
def combate(jugador, pokemon_salvaje):
    print("\n👾 ¡Ha aparecido un Pokémon salvaje!")
    pokemon_salvaje.mostrar_estado()

    while jugador.pokemon.hp > 0 and pokemon_salvaje.hp > 0:
        print("\nElige movimiento:")
        for i, mov in enumerate(jugador.pokemon.movimientos, start=1):
            print(f"{i}. {mov}")
        eleccion = input("> ")

        if eleccion.isdigit() and 1 <= int(eleccion) <= len(jugador.pokemon.movimientos):
            mov = jugador.pokemon.movimientos[int(eleccion)-1]
            jugador.pokemon.atacar(mov, pokemon_salvaje)
        else:
            print("❌ Opción no válida.")
            continue

        if pokemon_salvaje.hp > 0:
            mov_enemigo = random.choice(pokemon_salvaje.movimientos)
            pokemon_salvaje.atacar(mov_enemigo, jugador.pokemon)

        jugador.pokemon.mostrar_estado()
        pokemon_salvaje.mostrar_estado()

    if jugador.pokemon.hp > 0:
        print(f"\n🎉 {jugador.pokemon.nombre} ha derrotado a {pokemon_salvaje.nombre}!")
    else:
        print(f"\n💀 {jugador.pokemon.nombre} ha sido derrotado...")

# =========================
# BUCLE DEL JUEGO
# =========================
def jugar(jugador):
    mapa = Mapa()
    while True:
        mapa.dibujar(jugador)

        # Verificar si hay un Pokémon salvaje en la misma casilla
        for poke, x, y in mapa.pokemon_salvajes:
            if jugador.x == x and jugador.y == y:
                combate(jugador, poke)
                mapa.pokemon_salvajes.remove((poke, x, y))
                break

        comando = input("> ").lower()

        if comando == "w" and jugador.y > 0:
            jugador.y -= 1
        elif comando == "s" and jugador.y < mapa.alto - 1:
            jugador.y += 1
        elif comando == "a" and jugador.x > 0:
            jugador.x -= 1
        elif comando == "d" and jugador.x < mapa.ancho - 1:
            jugador.x += 1
        elif comando == "m":
            print("\n=== MENU DE ESTADO ===")
            jugador.pokemon.mostrar_estado()
            input("Presiona ENTER para volver...")
        elif comando == "q":
            guardar_partida(jugador)
            break

        # Posibilidad de que aparezca un Pokémon salvaje
        if random.random() < 0.2:  # 20% probabilidad
            mapa.generar_pokemon_salvaje()

# =========================
# INICIAR JUEGO
# =========================
if __name__ == "__main__":
    menu_principal()