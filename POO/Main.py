from Student import Alumno, Perro
def main():
    al1=Alumno("Brandon",19, "ICO")
    print(vars(al1))
    al1.__nombre="Bruno"
    print(vars(al1))
    # Use the method   
    al1.set_nombre("Isabel")
    print(vars(al1))

    print("-----------Use of To Strig------------")
    print(al1)

    al1.estudiar()

    # @property: A diferent way to impements encapsulation
    # @classmethod: Allow a declaration of class methods
    # @staticmethod: 

    print("------------Start class Perro-------------------")
    perro1= Perro("PODDLE", 2, 0.25)
    print(vars(perro1))
    perro1.raza="De la calle"
    print(vars(perro1))
    perro1.__raza="otra"#Set whit format Python
    print(vars(perro1))
    print(vars(perro1))
    perro1.edad=12
    perro1.estatura=0.43
    print(perro1)
    cachorro=Perro.es_cachoro(perro1.edad)
    # isn't necesari declarate a object to  
    print(cachorro)
    Perro.dormir()
    danes=Perro.perro_grande(0.8)
    print(danes)

    # CODIOGO DIA JUEVES
    

main()