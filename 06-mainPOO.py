# Program 05 that works whit the program 05 Stuffs.py
from 05_Student import Alumno

def main():

    """"
    al1=Alumno()
    print(al1)
    al2=Alumno()
    print(al1.faculdad)
    print(al2.faculdad)
    #W e can acces to the atrubut of the class
    print(Alumno.faculdad)
    print("-----------Modify ONLY the Student 1------------")
    # Add a atribute only a the object not to the class!
    al1.faculdad="FES Acatlan"
    #Whit this form we can modify the atrubut of the class!
    Alumno.faculdad="FES Cuautitlan"
    print(al1.faculdad)
    print(al2.faculdad)
    print(Alumno.faculdad)
    print("-----------Print the Objects------------")
    print(vars(al1))
    print(vars(al2))
    print("-----------Modify public atributs------------")
    al2.edad=999
    print(vars(al1))
    print(vars(al2))
    """
    #Creating Multiple students
    al1=Alumno("Brandon", 22, "Ing. en Computacion")
    al2=Alumno("Juan", 22, "Ing. en Computacion")
    print(al1.nombre)
    print(al1.edad)
    print(al1.carrera)

    print(al2.nombre)
    print(al2.edad)
    print(al2.carrera)
    # vars is very useful to print the objects when are encapsulating
    print(vars(al1))
    print(vars(al2))

    print(vars(al1))
    # Whit this we can think that the encapsulation doesn't work, but we are wrong
    # Python create a new atribute, but the original atribute is still encapsulated
    al1.__edad=333
    print (al1.__edad)
    print(vars(al1))


main()