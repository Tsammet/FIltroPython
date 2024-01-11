import json

def cargarFormatos():

    file = open("formatos.json")

    formatos = json.load(file)

    return formatos
    

def crearFormato():

    formatos = cargarFormatos()

    nuevoFormato = {}
    nuevoFormato["identificadorFormato"] = input("cuál es el identificador del formato que vas a registrar: ")
    nuevoFormato["nombreFormato"] = input("Cuál es el nombre del formato que vas a registrar: ")

    formatos.append(nuevoFormato)

    file = "formatos.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(formatos, file)
    
        # AGREGAR NUEVO DATO
        

def listarFormatos():

    formatos = cargarFormatos()

    for formato in formatos:

        if len(formatos) > 0:

            print("------------------------")

            print("Id: {} | Nombre: {}".format(formato["identificadorFormato"], formato["nombreFormato"]))

            print("------------------------")



