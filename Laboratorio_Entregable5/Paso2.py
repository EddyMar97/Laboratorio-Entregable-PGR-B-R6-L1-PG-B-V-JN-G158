# Parte 1
Valor = int(input("Ingresar un número: "))

if Valor  % 2 == 0:
    print(f"El número {Valor} es par.")
else: 
    print (f"El número {Valor} es inpar.")

# Parte 2
for Valor in [0,1,2,3,4,5,6,7,8,9,10]:
    Cuadrado = Valor**2
    print ("El cuadrado de", Valor, "es:",Cuadrado)

# Parte 3
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