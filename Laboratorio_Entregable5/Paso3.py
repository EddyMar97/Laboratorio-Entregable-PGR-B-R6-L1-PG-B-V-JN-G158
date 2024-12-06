# Parte 1
Estudiantes = ["Jose", "Pepito", "Andrea", "Kelly", "Antonio"]

Lista = 0

while Lista < len (Estudiantes):
    print ("Estudiante #",Lista+1,":", Estudiantes[Lista])
    Lista +=1

# Parte 2 y 3
Diccionario={
    "Nombre":"Eddy",
    "Apellido":"Martinez",
    "Edad": 27,
    "Ciudad":"Barranquilla",
    "Email":"eddy.martinez.ttc.964@unilibre.edu.co"
}

print("Información de contacto: ", Diccionario)

Diccionario["Profesión: "] = "Programador"
print("Nueva entrada: ", Diccionario)

Diccionario ["Edad"] = 30
print("Se modificó la edad: ", Diccionario["Edad"])
