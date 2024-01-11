from peliculas import cargarPeliculas

def listarPeliculasGenero():

    peliculas = cargarPeliculas()

    generoPregunta = input("Que peliculas deseas saber cuáles hay según su genero: ")

    for pelicula in peliculas: 

        if generoPregunta == pelicula["generoPelicula"]:

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
        

            print("-----------------")


def listarJhonnyDeep():

    peliculas = cargarPeliculas()

    for pelicula in peliculas:

        if "JHONNY DEEP" in pelicula["actoresPelicula"]:
            
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
        

            print("-----------------")


def buscarPeliculaSinopsis():
        
    peliculas = cargarPeliculas()

    preguntarPelicula = input("Cuál es la pelicula que está buscando: ")

    for pelicula in peliculas:

        if preguntarPelicula == pelicula["nombrePelicula"]:

            print("------------------------")

            print("La pelicula que usted está buscando se encuentra aquí.")

            print("------------------------")

            
            print("NOMBRE: {}".format(pelicula["nombrePelicula"]))
            print("SINOPSIS: {}".format(pelicula["sinopsisPelicula"]))
            print("ACTORES: {}".format(pelicula["actoresPelicula"]))
            

            print("------------------------")


        else:

            print("No se encuentra la pelicula")