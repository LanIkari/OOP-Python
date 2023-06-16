class Libro:
    # Constructor
    def __init__(self,tit, aut, an, ed):
        self.__titulo=tit
        self.__autor=aut
        self.__año=an
        self.__editorial=ed
    #DECORADORES

    #GET TITULO
    def titulo(self):
        return self.__titulo
    
    #constructor
    def __str__(self):
        return f"""
        -------------------------DETAELLES DEL LIBRO-------------------------
        Titulo= {self.__titulo} 
        Autor= {self.__autor}
        Año= {self.__año}
        Editoril= {self.__editorial}
        ---------------------------------------------------------------------\n"""
    
    # METODO LEER
    @classmethod
    def leer(self,minutos):
        print(f"Leyendo por {minutos} minutos")
    
    @classmethod
    def libro_planeta(cls,titulo,autor,año):
        return cls(titulo,autor,año,"Planeta")

class Autor:
    # Constructor
    def __init__(self,nom,pseudo):
        self.__nombre=nom
        self.__pseudonimo=pseudo
    #Decoradores

    #GET NOMBRE
    @property
    def nombre(self):
        return self.__nombre
    #SET NOMBRE
    @nombre.setter
    def nombre(self, nom):
        self.__nombre=  nom
    #GET PSEUDONIMO
    @property
    def pseudonimo(self):
        return self.__pseudonimo
    #SET PSEUDONIMO
    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo=  pseudo
    #METODO TOSTRING
    def __str__(self):
        return f"Nombre: {self.__nombre} Pseudonimo: {self.__pseudonimo}"
    
    #Metodo escribir
    def escribir(self):
        print(f"{self.__pseudonimo} esta escribiendo su siguiente libro")


class Persona:
    def __init__(self, nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom
    # ----------------------HERENCIA----------------------

class Alumno(Persona):
    def __init__ (self, nombre, edad, num_cuenta, carrera,promedio):
        super().__init__(nombre,edad)
        self.__num_cuenta=num_cuenta
        self.__carrera=carrera
        self.__promedio=promedio