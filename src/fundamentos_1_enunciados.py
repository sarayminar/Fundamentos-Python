# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
# a = "Hola"
# b = 25
# c = 3.14
# d = True
# e = None


a = "Hola"
b = 25
c = 3.14
d = True
e = None

type(a)
type(b)
type(c)
type(d)
type(e)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"


cadena = "42"
numero = int(cadena) + 8    
print(numero)
numero = 100
cadena = str(numero)
print("Tu puntuación final es: " + cadena)

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

nombre = "Marta"
edad = 30
print("Hola, me llamo " + nombre + " y tengo " + str(edad) + " años.")

#print(f"Hola, {nombre}")


# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
# x = "gato"
# y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

x = "gato"
y = "perro"


x, y = y, x

print("x:", x)
print("y:", y)  


# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
# pan = 1.50
# leche = 1.24
# huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

pan = 1.20
leche = 0.95
huevos = 2.10
total = pan + leche + huevos
print("Te has gastado un total de: " + str(total) + "€ hoy en tu compra.")

# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.

numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")  
else:
    print("El número es impar.")

# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.


age = int(input("Dime tu edad: "))

if age >= 18:
    print("Puedes entrar.")
else:
    print("Acceso denegado.")


# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.


choice = int(input("Elige una opción entre: 1, 2 y 3: "))
if choice == 1:
    print("Has elegido ver tu perfil.")
elif choice == 2:
    print("Has elegido editar tu perfil.")
elif choice == 3:
    print("Has elegido cerrar sesión.")
else:
    print("No hay número para esa opción.")


# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().


mensaje = input("Escribe algo: ")

try:
    dato = int(mensaje)
    print("Has escrito un número entero")

except ValueError:
    if isinstance(mensaje, float):
        print("Has escrito un número decimal")
    elif isinstance(mensaje, str):
        print("Parece que es una cadena de texto")
    else:
        print("No sé qué es esto")


# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.


edad = int(input("Introduce tu edad: "))

if edad < 3:
    print("Eres un bebé.")
elif edad >= 3 and edad <= 12:
    print("Estás en la infancia.")
elif edad >= 13 and edad <=17:
    print("Estás en la adolescencia.")
elif edad >= 18 and edad <=64:
    print("Estás en la adultez")
elif edad >= 64:
    print("Estás en la vejez.")
else:
    print("No has introducida una edad válida.")




# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”


numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

menu = int(input("Escribe 1 para sumar, 2 para restar, 3 para multiplicar o 4 para dividir: "))
if menu == 1:
    operacion = numero1 + numero2
    print("El resultado de tu suma es: " + operacion)
elif menu == 2:
    operacion = numero1 - numero2
    print("El resultado de tu resta es: " + operacion) 
elif menu == 3:
    operacion = numero1 * numero2
    print("El resultado de tu multiplicación es: " + operacion)
elif menu == 4: 
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        operacion = numero1 / numero2
        print("El resultado de tu division es: " + operacion)

