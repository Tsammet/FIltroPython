from menuSecundario import menuGeneros, menuActores, menuFormatos, menuPeliculas, menuInformes

def menuPrincipal():

    salir = False



    while not salir:


            pregunta = int(input("1. Administrador de generos.\n"
                                "2. Administrador de actores. \n"
                                "3. Administrador de formatos. \n"
                                "4. Gestor de peliculas. \n"
                                "5. Gestor de informes. \n"
                                "6. Salir. \n"
                                "Que opción deseas elegir: "))

            match pregunta:
                
                case 1:
                    
                    menuGeneros()

                case 2:

                    menuActores()

                case 3:

                    menuFormatos()

                case 4:

                    menuPeliculas()
                
                case 5:
                      
                    menuInformes()
                      

                case 6:
                      
                      print("Hasta luego que tenga un buen día")
                      salir = True
                      
                

                
        

menuPrincipal()