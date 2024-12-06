# Parte 1
Valor1 = int(input("Ingresar número: "))
Valor2 = int(input("Ingresar otro número: "))

Sumar = Valor1 + Valor2
Restar = Valor1 - Valor2
Multi = Valor1 * Valor2
Divi = Valor1 / Valor2

print (f"Concatenación: \nLa suma de: {Valor1} + {Valor2} es igual a: {Sumar}\nLa resta de: {Valor1} - {Valor2} es igual a: {Restar}\nLa multiplicación de: {Valor1} * {Valor2} es igual a: {Multi}\nLa división de: {Valor1} / {Valor2} es igual a: {Divi}")

# Parte 2
import random
Aleatorio = random.randint(1, 50)
Adivina = -1
while Adivina != Aleatorio:
    Preguntar = input("Adivina el número!\nIngresa un número del 1 al 50: ")
    Adivina = int(Preguntar)

    if Adivina < Aleatorio:
        print("Estás por debajo del número ganador! Sigue intentando")
    elif Adivina > Aleatorio:
        print("Estás por encima del número ganador! Sigue intentando")

print(f"Has adivinado! '{Aleatorio}' es el número ganador, felicidades!")