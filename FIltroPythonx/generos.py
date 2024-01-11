import json

def cargarGeneros():

    file = open("generos.json")

    generos = json.load(file)

    return generos
    

def crearGenero():

    generos = cargarGeneros()

    nuevoGenero = {}

    # nuevoGenero["identificadorGenero"] = input("cuál es el identificador del genero que vas a registrar: ")
    nuevoGenero["identificadorGenero"] = input("Cuál es el identificador del genero que vas a registrar: ")
    nuevoGenero["nombreGenero"] = input("Cuál es el nombre del genero que vas a registrar: ")



    generos.append(nuevoGenero)

    file = "generos.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(generos, file)
    
        # AGREGAR NUEVO DATO
        

def listarGeneros():

    generos = cargarGeneros()

    for genero in generos:

        if len(generos) > 0:

            print("------------------------")

            print("Id: {} | Nombre: {}".format(genero["identificadorGenero"], genero["nombreGenero"]))

            print("------------------------")



