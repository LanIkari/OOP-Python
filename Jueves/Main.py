from Libreria import Libro, Autor, Alumno

def main():
    l1=Libro.libro_planeta("El señor de los anillos","J.R.R Tolkien",1954)
    print(l1)
    # -----------------PRUEBA HERENCIA-----------------
    al2=Alumno("Brandon",22, "316353087", "ICO", 9)
    # Metodo de acceso de la clase padre, que en este caso es la clase Persona
    al2.nombre="Brandon A.V"
    print(vars(al2))

main()