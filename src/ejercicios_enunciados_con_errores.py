# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)


# import csv

# films = {}

# def mostrar_menu():
#     print("🎬 Menú")
#     print("1️⃣  Añadir película")
#     print("2️⃣  Votar por una película")
#     print("3️⃣  Mostrar resultados")
#     print("4️⃣  Salir")
#     return input("❓ ¿Qué quieres hacer? (1-4): ")

# def add_film():
#     name = input("🎞️ Nombre de la película: ").strip()
#     year = input("📅 Año de estreno: ").strip()

#     if name in films:
#         print("⚠️ Esa película ya existe.")
#     else:
#         films[name] = {"year": year, "votes": 0}
#         print(f"✅ Película '{name}' añadida correctamente.")

# def vote_film():
#     name = input("🗳️ ¿A qué película quieres votar?: ").strip()
#     try:
#         films[name]["votes"] += 1
#         print(f"🟢 Voto registrado. '{name}' ahora tiene {films[name]['votes']} voto(s).")
#     except KeyError:
#         print("❌ Error: No se encuentra una película con ese nombre.")

# def show_results():
#     if not films:
#         print("📭 No hay películas registradas aún.")
#         return

#     print("📊 Resultados de la votación:")
#     for name, data in films.items():
#         print(f"  • {name} ({data['year']}): {data['votes']} voto(s)")

# def save_to_csv(filename="resultados_votaciones.csv"):
#     with open(filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Película", "Año", "Votos"])
#         for name, data in films.items():
#             writer.writerow([name, data["year"], data["votes"]])
#     print(f"💾 Resultados guardados en '{filename}'")

# # Programa principal
# def main():
#     while True:
#         option = mostrar_menu()
#         if option == "1":
#             add_film()
#         elif option == "2":
#             vote_film()
#         elif option == "3":
#             show_results()
#         elif option == "4":
#             save_to_csv()
#             print("👋 ¡Hasta luego!")
#             break
#         else:
#             print("🚫 Opción no válida. Intenta de nuevo.")

# # if __name__ == "__main__":
# main()



# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena (TypeError o AttributeError)

# def limpieza_nombres():
#     nombres_limpios = []
#     for nombre in nombres:
#         limpio = ' '.join(nombre.strip().split())  
#         limpio = limpio.title()  
#         nombres_limpios.append(limpio)

#     sin_duplicados = list(set(nombres_limpios))  
#     sin_duplicados.sort()  

#     print("🧼 Lista limpia y ordenada de nombres únicos:")
#     print(sin_duplicados)
#     print("🔢 El número de nombres únicos es:", len(sin_duplicados))

# nombres = [
#     "  juan Pérez",
#     "María  lopez",
#     "Carlos garcía",
#     "ANA MARTINEZ",
#     "  juan Pérez",
#     "luis fernandez",
#     "Luis   Fernandez",
#     "Pedro Gómez",
#     "pedro gómez",
#     "MARTA   suarez",
#     "marta Suarez",
#     "  José  ramirez",
#     "josé Ramirez",
#     "Clara  MEJIA",
#     "clara mejia"
# ]

# limpieza_nombres()

# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

# parrafo = str(input("📝 Introduce un párrafo: "))

# palabras = parrafo.split()
# cantidad = len(palabras)
# print("🔠 Tu párrafo tiene ", cantidad, " de palabras")


# import string
# from collections import Counter

# parrafo = input("📝 Introduce un párrafo: ").strip()

# if not parrafo:
#     raise ValueError("⚠️ El párrafo no puede estar vacío.")


# parrafo_limpio = parrafo.translate(str.maketrans("", "", string.punctuation)).lower()
# palabras = parrafo_limpio.split()


# cantidad = len(palabras)
# print("🔢 Tu párrafo tiene", cantidad, "palabras.")


# frecuencias = Counter(palabras)

# print("\n📊 Frecuencia de palabras:")
# for palabra, veces in frecuencias.items():
#     print(f"🟩 '{palabra}': {veces} vez/veces")

# palabra_mas_repetida = frecuencias.most_common(1)[0]
# print(f"\n🏆 La palabra más repetida es: '{palabra_mas_repetida[0]}' ({palabra_mas_repetida[1]} veces)")

 

# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar si el producto no existe.

# inventario = []

# def mostrar_menu():
#     print("\n📋 --- Menú de Inventario ---")
#     print("1️⃣  Añadir producto")
#     print("2️⃣  Actualizar stock")
#     print("3️⃣  Eliminar producto")
#     print("4️⃣  Ver inventario")
#     print("5️⃣  Salir")
#     try:
#         return int(input("❓ ¿Qué quieres hacer?: "))
#     except ValueError:
#         print("⚠️ Por favor, introduce un número válido.")
#         return 0

# def añadir_producto():
#     nombre = input("🛒 Nombre del producto: ")
#     try:
#         precio = float(input("💰 Precio: "))
#         stock = int(input("📦 Stock: "))
#         # Verificar si ya existe
#         for producto in inventario:
#             if producto["nombre"] == nombre:
#                 print("⚠️ Ese producto ya existe.")
#                 return
#         inventario.append({"nombre": nombre, "precio": precio, "stock": stock})
#         print(f"✅ {nombre} se añadió correctamente.")
#     except ValueError:
#         print("⚠️ Precio o stock no válido.")

# def actualizar_stock():
#     nombre = input("🔄 ¿Qué producto quieres actualizar?: ")
#     for producto in inventario:
#         if producto["nombre"] == nombre:
#             try:
#                 nuevo_stock = int(input("📥 Nuevo stock: "))
#                 producto["stock"] = nuevo_stock
#                 print(f"✅ Stock de '{nombre}' actualizado a {nuevo_stock}.")
#                 return
#             except ValueError:
#                 print("⚠️ Stock no válido.")
#                 return
#     print("❌ Producto no encontrado.")

# def eliminar_producto():
#     nombre = input("🗑️ ¿Qué producto quieres eliminar?: ")
#     for producto in inventario:
#         if producto["nombre"] == nombre:
#             inventario.remove(producto)
#             print(f"🧹 {nombre} eliminado correctamente.")
#             return
#     print("❌ Producto no encontrado.")

# def mostrar_inventario():
#     if inventario:
#         print("\n📦 --- Inventario actual ---")
#         for producto in inventario:
#             print(f"🔹 {producto['nombre']} - 💰 Precio: {producto['precio']} - 📦 Stock: {producto['stock']}")
#     else:
#         print("📭 El inventario está vacío.")

# def ejecutar_menu():
#     while True:
#         opcion = mostrar_menu()
#         if opcion == 1:
#             añadir_producto()
#         elif opcion == 2:
#             actualizar_stock()
#         elif opcion == 3:
#             eliminar_producto()
#         elif opcion == 4:
#             mostrar_inventario()
#         elif opcion == 5:
#             print("👋 Saliendo del sistema...")
#             break
#         else:
#             print("⚠️ Opción no válida.")

# ejecutar_menu()



# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)


# import random, string

# def generar_alias():
#     try:
#         nombre = str(input("📝 Introduce un nombre: "))
#         apellido = str(input("📝 Introduce un apellido: "))

#         if type(nombre) or type(apellido) != type(str):
#             raise ValueError("🚫 No es el tipo que se espera")
#         if len(nombre) < 2:
#             raise ValueError("⚠️ El nombre debe tener al menos 2 letras.")
#         if len(apellido) < 3:
#             raise ValueError("⚠️ El apellido debe tener al menos 3 letras.")

#         nombre_modificado = nombre[0] + nombre[1] 
#         apellido_modificado = apellido[0] + apellido[1] + apellido[2]
#         numero = str(random.choice(range(10, 100)))
#         simbolo = str(random.choice(list('!@#$%&*')))

#         alias = nombre_modificado + apellido_modificado + numero + simbolo
#         print("🆔 Tu alias es:", alias)

#     except ValueError as e:
#         print(f"❌ Error: {e}")
     
# generar_alias()

# def generar_contraseña(longitud):
#     if longitud < 8:
#         print("⚠️ La longitud mínima debe ser 8 caracteres.")
#         return None

#     minusculas = list(string.ascii_lowercase)
#     mayusculas = list(string.ascii_uppercase)
#     numeros = list(string.digits)
#     simbolos = list('!@#$%&*')

#     contraseña = [random.choice(minusculas),
#                   random.choice(mayusculas),
#                   random.choice(numeros),
#                   random.choice(simbolos)]
    
#     lista_completa = minusculas + mayusculas + numeros + simbolos

#     longitud_restante = longitud - len(contraseña)
#     contraseña += random.choices(lista_completa, k=longitud_restante)
#     random.shuffle(contraseña)
#     return ''.join(contraseña)

# print("🔐 LA CONTRASEÑA ES:", generar_contraseña(12))




# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

# def comprobar_contrasena():
#     try:
#         contrasena = input("🔑 Introduce la contraseña: ")

#         if len(contrasena) < 8:
#             raise ValueError("⚠️ La contraseña debe tener al menos 8 caracteres")
#         if not any(c.isupper() for c in contrasena):
#             raise ValueError("⚠️ La contraseña debe tener al menos una mayúscula")
#         if not any(c.islower() for c in contrasena):
#             raise ValueError("⚠️ La contraseña debe tener al menos una minúscula")
#         if not any(c.isdigit() for c in contrasena):
#             raise ValueError("⚠️ La contraseña debe tener al menos un número")

#         print("✅ Contraseña válida.")

#     except ValueError as e:
#         print(f"❌ Error: {e}")

# comprobar_contrasena()


# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)
 
import random

habitaciones = list(range(101, 111))
reservas = {}

def menu_hotel():
    while True:
        print("🏨 Habitaciones del 101 al 110, ¿qué deseas hacer?")
        print("1️⃣ Ver habitaciones disponibles")
        print("2️⃣ Reservar habitación (introduciendo su nombre)")
        print("3️⃣ Cancelar reserva")
        print("4️⃣ Ver reservas confirmadas")
        print("5️⃣ Salir")

        opcion = input("📋 Introduce una opción (1-5): ")

        if opcion == "1":
            ver_habitaciones()
        elif opcion == "2":
            reservar_habitacion()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            ver_reservas()
        elif opcion == "5":
            print("👋 ¡Hasta pronto!")
            break  # Sale del bucle y termina el programa
        else:
            print("❌ Opción no válida, intenta de nuevo.\n")


def ver_habitaciones():
    print("🔍 Aquí tienes las habitaciones disponibles:")
    for habitacion in habitaciones:
        if habitacion in reservas:
            print(f"❌ Lo siento, la habitación {habitacion} está ocupada")
        else:
            print(f"✅ La habitación {habitacion} está disponible")
    print()
    

def reservar_habitacion():
    try:
        num = int(input("🔢 Ingrese el número de habitación a reservar (101-110): "))
        if num not in habitaciones:
            raise KeyError("🛏️❌ Habitación inválida.")
        if num in reservas:
            print("⚠️ Esa habitación ya está ocupada.")
        else:
            nombre = input("✍🏻Ingrese su nombre: ")
            reservas[num] = nombre
            print(f"🛏️✅ Habitación {num} reservada exitosamente por {nombre}.\n")
    except KeyError as e:
        print(f"❌ Error: {e}\n")
    except ValueError:
        print("❌ Error: Ingrese un número válido.\n")

def cancelar_reserva():
    try:
        num = int(input("🛏️ Ingrese el número de habitación a cancelar (101-110): "))
        if num not in habitaciones:
            raise KeyError("🛏️❌ Habitación inválida.")
        if num in reservas:
            del reservas[num]
            print(f"✅ Reserva en la habitación {num} ha sido cancelada.\n")
        else:
            print("⚠️ Esa habitación no tiene ninguna reserva.\n")
    except KeyError as e:
        print(f"❌ Error: {e}\n")
    except ValueError:
        print("❌ Error: Ingrese un número válido.\n")


def ver_reservas():
    if reservas:
        print("\n📑 Reservas confirmadas:")
        for habitacion, nombre in sorted(reservas.items()):
            print(f"Habitación {habitacion}: {nombre}")
    else:
        print("🔍 No hay reservas confirmadas.")
    print()

menu_hotel()