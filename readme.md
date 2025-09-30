🎮 Descripción

El jugador puede:
	•	Crear una partida nueva.
	•	Guardar y continuar su progreso.
	•	Borrar partidas guardadas.
	•	Explorar un mapa en ASCII (cuadrado).
	•	Encontrar criaturas salvajes 👾 y combatir contra ellas.
	•	Usar diferentes movimientos en combate.

⸻

🧩 Conceptos de POO aplicados

El código aplica los principales conceptos de Programación Orientada a Objetos:

Clases
	•	Movimiento: representa un ataque con nombre, poder y tipo.
	•	Pokimonii: representa a una criatura con atributos como nombre, tipo, hp, movimientos y arte ASCII.
	•	Jugador: almacena el estado del jugador, su pokimoniii y su posición en el mapa.
	•	Mapa: gestiona el tablero cuadrado, dibuja el entorno y coloca criaturas salvajes.

Objetos e Instancias
	•	Cada vez que se crea un pokimoniii o un movimiento, se genera un objeto único a partir de su clase.
	•	Ejemplo:

garfang = pokimoniii("Garfang", "Bestia", 40, [...], arte)



Herencia

En este caso se usa principalmente composición (pokimoniii que contienen movimientos), pero el diseño se pensó para que nuevas clases de criaturas pudieran heredar de pokimoniii en el futuro.

Polimorfismo

Los movimientos (Movimiento) se usan de forma polimórfica, ya que cada uno tiene un nombre, poder y tipo distintos, pero todos se ejecutan con el mismo método .atacar().

Encapsulamiento

Cada clase agrupa sus atributos y comportamientos en un mismo bloque, separando responsabilidades:
	•	El Mapa solo se encarga de mostrar y generar criaturas.
	•	El Jugador maneja su pokimoniii y su posición.
	•	El pokimoniii maneja vida, ataques y estados.

⸻

📂 Estructura del proyecto

juego_criaturas/
│── main.py        # Código principal del juego
│── sombrachu.dat  # Ejemplo de partida guardada
│── README.md      # Este archivo


⸻

🚀 Cómo ejecutar
	1.	Asegúrate de tener Python 3 instalado.
	2.	Descarga o clona el repositorio.
	3.	Ejecuta el archivo:

python main.py


	4.	Disfruta explorando el mapa y combatiendo criaturas.

⸻

✨ Ejemplo en consola

Mapa cuadrado:

. . . . . . . . . . 
. . . . . . . . . . 
. . 👾 . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . 😀 . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 

Combate:

👾 ¡Ha aparecido un pokimoniiiu salvaje!

Garfang (Bestia) - HP: 40/40
 /\_/\
( o.o )≡
 > ^ <

Elige movimiento:
1. Arañazo Feroz (Poder: 8, Tipo: Bestia)
2. Mordida (Poder: 10, Tipo: Bestia)
3. Garra Oscura (Poder: 12, Tipo: Sombra)
4. Zarpazo Final (Poder: 15, Tipo: Bestia)


⸻

📖 Notas finales

Este proyecto fue realizado con fines educativos para practicar Programación Orientada a Objetos (POO).