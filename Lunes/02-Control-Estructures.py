# if
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")

# if-esle

edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# if- elif - else
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")

# if-elif-elif
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un joven adulto.")


# For   for(int = 1 ; i<10 ; i++)

for i in range(1, 10, 1):
    print(i)

frutas = ['piña', 'pera', 'manzana', 'fresa', 'aguacate']
for numero in frutas:
    print(numero)

for numero in frutas:
    if numero == "manzana":
        break   # ó continue
    print(numero)  # imprime la fruta

#While
tam=0
while tam<0:
    print(tam)
    tam=int(input("Ingrese un numero entero:"))