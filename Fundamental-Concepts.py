# Esto es un comentario
print("Hola Mundo")  # Esto imprime "Hola Mundo"

print("Hola", "Mundo")

print("Hola" + "Mundo")

print("Hola", "Mundo", sep="-")  # Imprime: Hola-Mundo

print("Hola", end="")
print("Mundo")  # Imprime: HolaMundo


nombre = "Brandon"
carrera = "Ingeneria en Computacion, la mejor"
print("Mi nombre es {} y estudio {} en la FES Aragón".format(nombre, carrera))


nombre = "Brandon"
carrera = "Ingeneria en Computacion, la mejor"
print(f"Mi nombre es { nombre} y estudio { carrera } en la FES Aragón")


"""
este es
un 
comentario de
múltiple línea
"""

# Operadores aritméticos
suma = 5 + 3    # 8
resta = 5 - 3   # 2
producto = 5 * 3  # 15
division = 5 / 3  # 1.66667
division2 = 5 // 3  # 1
modulo = 5 % 3   # 2
potencia = 5 ** 3  # 125

# Operadores de comparación
igual = 5 == 3  # False
diferente = 5 != 3  # True
mayor_que = 5 > 3  # True
menor_que = 5 < 3  # False
mayor_o_igual_que = 5 >= 3  # True
menor_o_igual_que = 5 <= 3  # False

# Operadores lógicos
y = True and False  # False
o = True or False  # True
no = not True  # False

saludo = "Hola Mundo"
cita = 'Los alumnos de ICO dicen: "Hola Mundo"'
parrafo = """Esto es un párrafo
que abarca varias
líneas"""


def fn_uno():
    print("Hola")


a, b, c = 10, "Hola", [2.3, 3.4]
print(a)
print(b)
print(c[1])


# entrada por teclado
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola {nombre}!")

edad = int(input("Introduce tu edad:"))
print(f"{nombre} tiene {edad} años")


mensaje = "Hola Mundo"  # String
edad = 20               # Integer
pi = 3.14159            # Float
es_mayor = True         # Boolean
imaginario = 3 + 4j     # Imaginario


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
