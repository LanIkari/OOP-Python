#Program 05

# Definet a empty class
class Alumno:
    # Atrubut of class
    faculdad="FES Aragon"
    # Constructor
    def __init__(self, nom, ed, carr):
        # Whit this notation we don't have encapsulation
        self.nombre=nom
        self.edad=ed
        self.carrera=carr
        # Private atributes be declared with __
        self.__nombre=nom
        self.__edad=ed
        self.__carrera=carr

#Encapsulation

#Builder overload