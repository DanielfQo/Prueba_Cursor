#programa para hacer operaciones basicas de calculadora

#1. pide al usuario la operacion que desea realizar
#2. pide al usuario dos numeros para la operacion

#3. realizar operacion y mostrar el resultado

#4. repetir el proceso hasta que el usuario lo indique salir

operacion = input("Introduce la operacion que desea realizar: ")
while operacion != "salir":
  numero1 = float(input("Introduce el primer numero: "))
  numero2 = float(input("Introduce el segundo numero: "))
  if operacion == "sumar":
    resultado = numero1 + numero2
  elif operacion == "restar":
    resultado = numero1 - numero2
  elif operacion == "multiplicar":
    resultado = numero1 * numero2
  elif operacion == "dividir":
    resultado = numero1 / numero2
  print(f"El resultado de la operacion es: {resultado}")
  operacion = input("Introduce la operacion que desea realizar: ")
print("Gracias por usar la calculadora")