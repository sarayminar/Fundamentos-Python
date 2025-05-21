# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.

def saludar():
    print("¡Hola, bienvenido/a!")
saludar()

# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre) que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.

def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("saray")

# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().

def suma (a,b):
    suma = a + b
    print(f"El resulado de la suma es: {suma}")

suma(2,5)

# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y False si es impar.
# Pruébala con varios números y muestra el resultado.

def par_impar(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print ("Es impar")

par_impar(7)
par_impar(2)

# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().

def mensaje(nombre, edad):
    print("Me llamo ", nombre, " y tengo", edad, " años" )
mensaje("Saray", 23)

# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede dividir por cero"
def sumar(a, b):
    suma = a + b

def restar(a, b):
    resta = a - b

def multiplicar(a, b):
    multiplicacion = a * b

def dividir(a, b):
    division = a / b

# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la edad que tendrás después de X años.


def edad_futura(edad_actual, años):
    edad_f = edad_actual + años
    return edad_f

print(edad_futura(25, 10))  

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c) que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

def calcular_media (a, b, c):
    media = (a + b + c) / 3
    return media
print("La media es ", calcular_media(2, 5, 78))


# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión

def mostrar_menu():
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Cerrar sesión")
mostrar_menu()



# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

import random, string

def generar_contraseña(longitud):

    if longitud < 8:
        print("⚠️ La longitud mínima debe ser 8 caracteres.")
        return None


    minusculas = list(string.ascii_lowercase)
    mayusculas = list(string.ascii_uppercase)
    numeros = list(string.digits)
    simbolos = list('!@#$%&*')

    contraseña = [random.choice(minusculas),
                  random.choice(mayusculas),
                  random.choice(numeros),
                  random.choice(simbolos)]
    
    lista_completa = minusculas + mayusculas + numeros + simbolos

    longitud_restante = longitud - len(contraseña)
    contraseña += random.choices(lista_completa, k=longitud_restante)
    random.shuffle(contraseña)
    return ''.join(contraseña)

print ("LA CONTRASEÑA ES: ", generar_contraseña(12))








    