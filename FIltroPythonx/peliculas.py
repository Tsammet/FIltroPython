from actores import cargarActores
from generos import cargarGeneros
from formatos import cargarFormatos
import json

def cargarPeliculas():

    file = open("peliculas.json")

    peliculas = json.load(file)

    return peliculas
    

def crearPelicula():

    peliculas = cargarPeliculas()
    generos = cargarGeneros()
    actores = cargarActores()
    formatos = cargarFormatos()

    nuevaPelicula = {}

    nuevaPelicula["idPelicula"] = input("Cuál es el id de la pelicula que vas a registrar: ")
    nuevaPelicula["nombrePelicula"] = input("Cuál es el nombre de la pelicula que vas a registrar: ")
    nuevaPelicula["duracionPelicula"] = input("Cuál es la duracion de la pelicula: ")
    nuevaPelicula["sinopsisPelicula"] = input("Cuál es la sinopsis de la pelicula que vas a registrar: ")
    generoPregunta = input("Cuál es el nombre del genero de la pelicula: ")
    nuevaPelicula["actoresPelicula"] = []
    formatoPregunta = input("Cuál es el formato de la pelicula: ")

    for formato in formatos:

        if formato["nombreFormato"] == formatoPregunta:

            nuevaPelicula["identificadorFormato"] = formato["identificadorFormato"]
            nuevaPelicula["formatoPelicula"] = formato["nombreFormato"]
            

    for genero in generos:

        if generoPregunta == genero["nombreGenero"]:

            nuevaPelicula["idGenero"] = genero["identificadorGenero"]
            nuevaPelicula["generoPelicula"] = genero["nombreGenero"]

            

    
    for actor in actores:

        salir = False

    
        while not salir:

            opcionActor = int(input("1. Si desea ingresarle un actor a la pelicula \n"
                            "2. Si desea salir \n"
                            "Que opción eligirás : "))
            
            match opcionActor:

                case 1: 

                    actorPregunta= input("Cuál es el nombre del que actor aparece en la pelicula")

                    if actorPregunta == actor["nombreActor"]:

                        nuevaPelicula["identificadorActor"] = actor["identificadorActor"]
                        nuevaPelicula["actoresPelicula"].append(actorPregunta)
                    
                    else:

                        print("El actor no se encuentra registrado. ")

                    opcionActor = input("1. Si desea ingresarle un actor a la pelicula \n"
                            "2. Si desea salir \n"
                            "Que opción eligirás : ")
                
                case 2:

                    salir = True

            opcionActor = int(input("1. Si desea ingresarle un actor a la pelicula \n"
                            "2. Si desea salir \n"
                            "Que opción eligirás : "))

    peliculas.append(nuevaPelicula)
    

    file = "peliculas.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(peliculas, file)
    
        # AGREGAR NUEVO DATO


def editarPelicula():
    
    peliculas = cargarPeliculas()

    peliculaEditar = input("Cuál es el nombre de la pelicula que desea editar: ")

    for pelicula in peliculas:

        if peliculaEditar == pelicula["nombrePelicula"]:

            opcionEditar = int(input("0. NO EDITAR. \n"
                                    "1. ID . \n"
                                    "2. NOMBRE. \n"
                                    "3. DURACION. \n"
                                    "4. SINOPSIS. \n"
                                    "5. ID ACTOR. \n"
                                    "6. ACTORES. \n"
                                    "7. IDENTIFICADOR FORMATO. \n"
                                    "8. NOMBRE FORMATO. \n"
                                    "9. ID GENERO. \n"
                                    "10. NOMBRE GENERO. \n"
                                    "¿Qué opción desea editar?: "))
            
            while opcionEditar != 0:

                match opcionEditar:
                    case 1:
                        pelicula["idPelicula"] = input("Ingrese el nuevo Id: ")
                        break
                                
                    case 2:
                        pelicula["nombrePelicula"] = input("Ingrese el nuevo Nombre: ")
                        break

                    case 3:
                        pelicula["duracionPelicula"] = input("Cuál es la duracion: ")
                        break
                    
                    case 4:
                        pelicula["sinopsisPelicula"] = input("Cuál es su sinopsis: ")
                        break
                    
                    case 5:
                        pelicula["identificadorActor"] = input("Cuál es el identificador del Actor: ")
                        break
                
                    case 6:
                        pelicula["actoresPelicula"] = input("Cuál es el actor de la pelicula: ")
                        break
                    
                    case 7:
                        pelicula["identificadorFormato"] = input("cuál es el identificador del formato: ")
                        break

                    case 8:
                        pelicula["formatoPelicula"] = input("Cuál es el formato de la pelicula")
                        break

                    case 9:
                        pelicula["idGenero"] = input("Cuál es el id del genero de la pelicula: ")
                        break

                    case 10:
                        pelicula["generoPelicula"] = input("Cuál es el genero de la pelicula: ")
                        break

    
    file = "peliculas.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(peliculas, file)
    
        # AGREGAR NUEVO DATO


def eliminarPelicula():

    peliculas = cargarPeliculas()

    preguntaEliminar = input("Cuál es el nombre de la pelicula que desea eliminar: ")

    for pelicula in peliculas:

        if preguntaEliminar == pelicula["nombrePelicula"]:
            peliculas.pop(pelicula)


def buscarPelicula():

    peliculas = cargarPeliculas()

    preguntarPelicula = input("Cuál es la pelicula que está buscando: ")

    for pelicula in peliculas:

        if preguntarPelicula == pelicula["nombrePelicula"]:

            print("------------------------")

            print("La pelicula que usted está buscando se encuentra aquí.")

            print("------------------------")

            print("ID: {}".format(pelicula["idPelicula"]))
            print("NOMBRE: {}".format(pelicula["nombrePelicula"]))
            print("DURACION: {}".format(pelicula["duracionPelicula"]))
            print("SINOPSIS: {}".format(pelicula["sinopsisPelicula"]))
            print("ACTORES: {}".format(pelicula["actoresPelicula"]))
            print("ID_ACTOR: {}".format(pelicula["identificadorActor"]))
            print("IDENTIFICADOR_FORMATO: {}".format(pelicula["identificadorFormato"]))
            print("FORMATOPELICULA: {}".format(pelicula["formatoPelicula"]))
            print("IDGENERO: {}".format(pelicula["idGenero"]))
            print("GENERO_PELICULA: {}".format(pelicula["generoPelicula"]))
        

            print("------------------------")

        else:

            print("------------------------")
            print("No se encuentra la pelicula disponible")
            print("------------------------")



def listarPeliculas():


    peliculas = cargarPeliculas()

    for pelicula in peliculas:

        if len(peliculas) > 0:

            print("------------------------")

            print("ID: {}".format(pelicula["idPelicula"]))
            print("NOMBRE: {}".format(pelicula["nombrePelicula"]))
            print("DURACION: {}".format(pelicula["duracionPelicula"]))
            print("SINOPSIS: {}".format(pelicula["sinopsisPelicula"]))
            print("ACTORES: {}".format(pelicula["actoresPelicula"]))
            print("ID_ACTOR: {}".format(pelicula["identificadorActor"]))
            print("IDENTIFICADOR_FORMATO: {}".format(pelicula["identificadorFormato"]))
            print("FORMATOPELICULA: {}".format(pelicula["formatoPelicula"]))
            print("IDGENERO: {}".format(pelicula["idGenero"]))
            print("GENERO_PELICULA: {}".format(pelicula["generoPelicula"]))
        

            print("------------------------")
