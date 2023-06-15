class Alumno:
    faculdad="FES Aragon"
    # Constructor
    def __init__(self, nom, ed, carr):
        # Private atributes be declared with __
        self.__nombre=nom
        self.__edad=ed
        self.__carrera=carr
    #Implements of Setters and Getters 
    def set_nombre(self, nom):
        self.__nombre=nom
    
    def get_nombre(self):
        return self.__nombre
    # EDAD
    def set_edad(self,ed):
        if ed>=8 and ed<120:
            self.__edad=ed
        else:
            print("Edad invalidad")
            self.__edad=0

    def get_edad(self):
        return self.__edad
    # CARRERA
    def set_carrera(self,carr):
        self.__carrera=carr

    def get_carrera(self):
        return self.__carrera

    # Implement of thethe method toString
    def __str__(self):
        cadena="nombre: "+self.__nombre
        cadena= cadena + "\nedad: "+str(self.__edad)
        cadena= cadena + "\ncarrera: "+str(self.__carrera)
        cadena=cadena + "\n-----------End of To Strig------------"
        return cadena
    
    #Start whit horas minimun ine hour
    def estudiar(self, horas=1):
        print (f"El alumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino="Canino"
    def __init__(self,raza,edad,estatura):
        self.__raza=raza
        self.__edad=edad
        self.__estatura=estatura
    
    #!USE OF DECORATIONS
    #Method to acces ged
    @property
    def raza(self):
        return self.__raza
    #Method to acces ged
    @raza.setter
    def raza(self,la_raza):
        self.__raza=la_raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,la_edad):
        if la_edad>0 and la_edad<20:
            self.__edad=la_edad
        else:
            print("Edad no valida")
            self.__edad=0
    @property
    def estatura(self):
        return self.__estatura
        

    @estatura.setter
    def estatura(self, la_estatura):
        if la_estatura>0.1 and la_estatura< 1.50:
            self.__estatura= la_estatura
        else:
            print("Edad no valida")
            self.__estatura=0


    def __str__(self):
        return f"""
        ---------------------------------
        | Raza: {self.__raza}           |
        | Edad: {self.__edad}           |
        | Estatura: {self.__estatura}   |
        ---------------------------------
        """

    @staticmethod
    def es_cachoro(edad):
        return edad<3
    
    @staticmethod
    def dormir(veces=5):
        for i in range(veces):
            print(f"Dando vuelta {i+1}")
        print("A mimir")

    @classmethod
    def perro_grande(cls,est):
        if est>0.79:
            return cls("",0,est,9)
        
    #CODIGO DIA JUEVES
    
