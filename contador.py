#programa para contar palabras en un archivo de texto
from collections import Counter
import re

#1. pedir al usuario la ruta del archivo de texto

#2. leer el contenido del texto

#3. separar en palabras

#4. contar el numero total de palabras

#5. mostrar la 10 palabras mas frecuentes y su conteo

archivo = input("Introduce la ruta del archivo de texto: ")
try:
  with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

    palabras = contenido.split()

    total_palabras = len(palabras)
    print(f"El archivo de texto tiene {total_palabras} palabras")
    palabras_frecuentes = Counter(palabras).most_common(10)
    for palabra, conteo in palabras_frecuentes:
        print(f"{palabra}: {conteo}")
except FileNotFoundError:

    print("El archivo especificado no existe.")

    exit(1)