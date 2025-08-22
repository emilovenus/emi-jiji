
def agregar_alumno():
    id_alumno = input("Ingrese el ID del alumno: ").strip()
    if any(alumno[0] == id_alumno for alumno in alumnos):
        print(" Este ID ya existe. Intente con otro.")
        return

    nombre = input("Ingrese el nombre completo: ").strip()
    edad = input("Ingrese la edad: ").strip()
    
    if not edad.isdigit():
        print(" La edad debe ser un número entero.")
        return
    edad = int(edad)

    calificaciones = []
    while True:
        nota = input("Ingrese una calificación (o 'fin' para terminar): ").strip()
        if nota.lower() == "fin":
            break
        try:
            calificaciones.append(float(nota))
        except ValueError:
            print(" Debe ingresar un número válido.")

    alumnos.append((id_alumno, nombre, edad, calificaciones))
    print(" Alumno agregado con éxito.")


def mostrar_alumnos():
    if not alumnos:
        print(" No hay alumnos registrados.")
        return
    print("\n Lista de Alumnos:")
    for id_alumno, nombre, edad, calificaciones in alumnos:
        print(f"ID: {id_alumno} | Nombre: {nombre} | Edad: {edad} | Calificaciones: {calificaciones}")


def calcular_promedio():
    id_alumno = input("Ingrese el ID del alumno: ").strip()
    for alumno in alumnos:
        if alumno[0] == id_alumno:
            calificaciones = alumno[3]
            if not calificaciones:
                print(" Este alumno no tiene calificaciones registradas.")
                return
            promedio = sum(calificaciones) / len(calificaciones)
            print(f" Alumno {id_alumno} - {alumno[1]} - Promedio: {promedio:.2f}")
            return
    print(" Alumno no encontrado.")


def eliminar_alumno():
    id_alumno = input("Ingrese el ID del alumno a eliminar: ").strip()
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno[0] != id_alumno]
    print(" Alumno eliminado con éxito." if any(alumno[0] == id_alumno for alumno in alumnos) else "⚠️ Alumno no encontrado.")


# ------------------ MENÚ PRINCIPAL ------------------

def menu():
    while True:
        print("\n=====  SISTEMA DE GESTIÓN DE ALUMNOS =====")
        print("1. Agregar alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Calcular promedio de un alumno")
        print("4. Eliminar alumno")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")

# Ejecutar programa
menu()
