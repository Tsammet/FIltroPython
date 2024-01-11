import json

def cargarActores():

    file = open("actores.json")

    actores = json.load(file)

    return actores
    

def crearActores():

    actores = cargarActores()

    nuevoActor = {}
    nuevoActor["identificadorActor"] = input("cuál es el identificador del actor que vas a registrar: ")
    nuevoActor["nombreActor"] = input("Cuál es el nombre del actor que vas a registrar: ")

    actores.append(nuevoActor)

    file = "actores.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(actores, file)
    
        # AGREGAR NUEVO DATO
        


def listarActores():

    actores = cargarActores()

    for actor in actores:

        if len(actores) > 0:

            print("------------------------")

            print("Id: {} | Nombre: {}".format(actor["identificadorActor"], actor["nombreActor"]))

            print("------------------------")
