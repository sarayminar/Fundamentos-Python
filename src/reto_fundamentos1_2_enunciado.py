# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir



def menu ():
    print("Menú de contactos")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar por nombre")
    print("4. Salir")
    opcion = int(input("¿Qué quieres hacer?"))
    return opcion


contactos = []

def add_contacto():
    nombre = str(input("Escribe tu nombre: "))
    edad = int(input("Escribe tu edad: "))
    ciudad = str(input("Escribe tu ciudad o pueblo: "))

    nuevo_contacto = {
    "name" : nombre,
    "age" : edad,
    "city" : ciudad
}
    contactos.append(nuevo_contacto)

def ver_contacto():
    if not contactos:
        print("No hay contactos aún.")
    for c in contactos:
        print(f"Nombre: {c['name']} – Edad: {c['age']} – Ciudad: {c['city']}")

def buscar_contacto():
    search = str(input("Introduce el nombre que quieras buscar: "))
    found = False

    for contacto in contactos: 
        if contacto.get("name") == search:
            for clave, valor in contacto.items():
                print(f"{clave}: {valor}", end=" ")
            print()
            found = True
    if not found:
        print("No encuentro un contacto con ese nombre")


def ejecutar_menu():
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
            print("Salimos de paseo")
            break 
        else:
            print("Esto no vale nena")

   
ejecutar_menu()   
    
    
    

    
# elif op == 2:
#     for contacto in contactos :
#         for clave, valor in contacto.items():
#             print(f"{clave}: {valor}", end=" ")
#         print()
#     menu()

# elif op == 3:
   
    
   
# elif op == 4:
#     print("Salimos del programa")
#     quit() 

# else:
#     print("Eso no es una opción válida")  
#     menu()




