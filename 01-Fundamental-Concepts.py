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

# Listas

alumno = {'numero_cuenta': 1232322, 'carrera': 'ICO',
          'direccion': {'calle': 'rancho seco', 'numero': 23},
          "telefonos": [5523232935, 5532323232]}
print(alumno['direccion']['calle'][3:6:1])
print(alumno['telefonos'])

# Un diccionario es dinamico
alumno['carrera'] = "Ingeneria en Computacion"
print(alumno)
