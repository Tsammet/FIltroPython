from generos import crearGenero, listarGeneros
from actores import crearActores, listarActores
from formatos import crearFormato, listarFormatos
from peliculas import crearPelicula, listarPeliculas, editarPelicula, eliminarPelicula, buscarPelicula
from informes import listarPeliculasGenero, listarJhonnyDeep, buscarPeliculaSinopsis

def menuGeneros():

    salir = False

    while not salir:

        pregunta = int(input("1. Crear un nuevo genero.\n"
                             "2. Listar generos.\n"
                             "3. Ir al menú principal. \n"
                             "Que opción deseas elegir: "))
        
        match pregunta:

            case 1:
                crearGenero()

            case 2:
                listarGeneros()

            case 3:

                salir = True

                print("--------------------------------")

def menuActores():

    salir = False

    while not salir:

        pregunta = int(input("1. Crear un nuevo actor.\n"
                             "2. Listar Actores.\n"
                             "3. Ir al menú principal. \n"
                             "Que opción deseas elegir: "))
        
        match pregunta:

            case 1:
                crearActores()

            case 2:
                listarActores()

            case 3:

                salir = True

                print("--------------------------------")
        

def menuFormatos():

    salir = False

    while not salir:

        pregunta = int(input("1. Registrar nuevo Formato. \n"
                             "2. Listar formatos. \n"
                             "3. Ir al menú principal. \n"
                             "Que opción deseas elegir: "))
        
        match pregunta:

            case 1:

                crearFormato()

            case 2:

                listarFormatos()

            case 3:

                salir = True

                print("--------------------------------")


def menuPeliculas():

    salir = False

    while not salir:

        pregunta = int(input("1. Agregar nueva pelicula. \n"
                             "2. Editar Pelicula. \n"
                             "3. Eliminar Pelicula. \n"
                             "5. Buscar Pelicula. \n"
                             "6. Listar todas las peliculas. \n" 
                             "7. Ir al menú principal. \n"
                             "Que opción deseas elegir: "))
        
        match pregunta:

            case 1:

                crearPelicula()

            case 2:

                editarPelicula()

            case 3:

                eliminarPelicula()

            
            case 5:

                buscarPelicula()

            case 6:

                listarPeliculas()

            case 7:

                salir = True

                print("--------------------------------")


def menuInformes():


    salir = False

    while not salir:

        pregunta = int(input("1. Listar peliculas genero especifico. \n"
                             "2. Listar peliculas dónde el protagonista sea Jhonny Deep. \n"
                             "3. Buscar pelicula y mostrar sinopsis y actores. \n"
                             "4. Ir al menú principal. \n"
                             "Que opción deseas elegir: "))
        
        match pregunta:
            
            case 1:

                listarPeliculasGenero()

            case 2:

                listarJhonnyDeep()
        
            case 3:

                buscarPeliculaSinopsis()

            case 4:
                salir = True