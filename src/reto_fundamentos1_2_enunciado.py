# 🌟 Reto: Gestor de contactos con estilo y buen rollo 😎

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1️⃣ Añadir contacto
# 2️⃣ Ver contactos
# 3️⃣ Buscar por nombre
# 4️⃣ Salir

def menu():
    print("\n📒 Menú de contactos 📒")
    print("1️⃣ Añadir contacto")
    print("2️⃣ Ver contactos")
    print("3️⃣ Buscar por nombre")
    print("4️⃣ Salir")
    try:
        opcion = int(input("👉 ¿Qué quieres hacer? Elige una opción (1-4): "))
    except ValueError:
        print("⚠️ Por favor, introduce un número válido (1-4).")
        return 0
    return opcion


contactos = []

def add_contacto():
    print("\n📝 Vamos a añadir un nuevo contacto:")
    nombre = input("👤 Escribe tu nombre: ")
    edad = int(input("🎂 Escribe tu edad: "))
    ciudad = input("🌍 Escribe tu ciudad o pueblo: ")

    nuevo_contacto = {
        "name": nombre,
        "age": edad,
        "city": ciudad
    }
    contactos.append(nuevo_contacto)
    print(f"✅ ¡Contacto de {nombre} añadido con éxito! 🎉")

def ver_contacto():
    print("\n📋 Lista de contactos:")
    if not contactos:
        print("😕 No hay contactos aún. ¡Añade alguno primero!")
    else:
        for c in contactos:
            print(f"👤 Nombre: {c['name']} – 🎂 Edad: {c['age']} – 🌍 Ciudad: {c['city']}")

def buscar_contacto():
    print("\n🔍 Vamos a buscar un contacto:")
    search = input("🔎 Introduce el nombre que quieras buscar: ")
    found = False

    for contacto in contactos:
        if contacto.get("name").lower() == search.lower():
            print("🎯 ¡Contacto encontrado!")
            for clave, valor in contacto.items():
                emoji = "👤" if clave == "name" else "🎂" if clave == "age" else "🌍"
                print(f"{emoji} {clave.capitalize()}: {valor}", end="  ")
            print()
            found = True
    if not found:
        print("❌ No encontré un contacto con ese nombre... ¿Seguro que lo escribiste bien? 🤔")

def ejecutar_menu():
    print("👋 ¡Bienvenido/a al Gestor de Contactos! 💬")
    op = 0
    while op != 4:
        op = menu()
        if op == 1:
            add_contacto()
        elif op == 2:
            ver_contacto()
        elif op == 3:
            buscar_contacto()
        elif op == 4:
            print("👋 ¡Hasta pronto! Gracias por usar el gestor de contactos. 🌟")
            break
        elif op == 0:
            continue
        else:
            print("🚫 Esa opción no es válida. ¡Intenta de nuevo! 😅")

# 🚀 Ejecutamos la app
ejecutar_menu()
