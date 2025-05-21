# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

lista = ["Leche", "Pan", "Huevos", "Galletas", "Queso"]
print("El primer elemento de la lista es " + lista[0] + " y el último elemento es " + lista[4])



# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

lista.append("Fruta")
lista.remove("Pan")
print("La lista actualizada queda como: ", lista)



# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

random = [2, 6 , 8, 21, 25, 5, 9, 26, 27, 18]
random.sort()
print("La lista ordenada queda así ", random)


# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordenada = (127,23)
print(coordenada)



# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

fijo = ("azul", "rojo", "amarillo")
#fijo[0] = "verde"
print(fijo)


# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

diccionario = {
    "nombre": "Saray",
    "edad" : 23,
    "pueblo" : "El Entrego"
}
print(diccionario)



# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

diccionario["pueblo"] = "Sama"
diccionario["hobbie"] = "Leer"
print(diccionario)



# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

for clave, valor in diccionario.items():
    print(clave + ":", valor)



# ------------------------------
# SETS
# ------------------------------


# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

names = {"Saray", "Saray", "Jose", "Diego", "Lorena", "Jennifer", "Diego", "Sergio", "Ana", "Sergio", "Nicolás", "Noemí"}
print(names)


# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

setA = { "Saray", "Lorena", "Ana", "Diego", "Jose","Rubén"}
setB = {"Diego", "Jose","Rubén"}
  
diferencia = setA.difference(setB)
print("Los nombres que salen en setA y no en setB son: ", diferencia)

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

personas = {
    "Saray" : ["leer", "escuchar musica", "kdramas"],
    "Lorena" : ["dormir", "ir al gimnasio", "videojuegos"]
}  
personas["saray"].append("dormir") 
print("Los hobbies de Saray son: ", personas["Saray"])
print("Los hobbies de Lorena son: ", personas["Lorena"])