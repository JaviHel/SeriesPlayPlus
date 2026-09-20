import random, time
from ui.carga_de_datos import *
from ui.ascii_frame import *
from estructuras.arbol_binario import BST


# CONFIGURACION PRINCIPAL
DATOS = cargar_json("datos/dataset_10.json")
SERIES = DATOS["series"]
LOOP = True
ANCHO_RECUADRO = 60
af = AsciiFrame(ANCHO_RECUADRO)

# Crear Arbol Binario De Busqueda Para Cada Opcion Del JSON
#str
title_bst = BST()
genre_bst = BST()
age_rating_bst = BST()

#int
year_bst = BST()
pop_metrics_bst = BST()
episode_average_bst = BST()
seasons_bst = BST()
episodes_bst = BST()



# Carga opciones que su dato es una string(Cadena de caracteres)
title_bst.load_str(SERIES, "title")
genre_bst.load_str(SERIES, "genre")
age_rating_bst.load_str(SERIES, "age_rating")

# Carga opciones que su dato es un int(Entero)
year_bst.load_int(SERIES, "year")
pop_metrics_bst.load_int(SERIES, "popularity_metrics")
episode_average_bst.load_int(SERIES, "episode_duration_average")
seasons_bst.load_int(SERIES, "seasons")
episodes_bst.load_int(SERIES, "episodes")



# JSON RECORDATORIO
"""
{
"title": "Family Guy",
"genre": "Animation",
"year": 1999,
"popularity_metrics": 79,
"episode_duration_average": 22,
"seasons": 23,
"episodes": 430,
"age_rating": "TV-14",
"is_finished": false
}
"""







# FUNCIONES DE IMPRESION EN PANTALLA
def imprimir_texto_ensanguchado(text, indent="c", separator=" "):
    """ Imprime Texto Dentro De Una Caja ASCII """
    af.print_box("t")
    af.print_text(text, indent, separator)
    af.print_box("b")


def imprimir_pantalla_ensanguchada(lst, indent="l"):
    """ Imprime una lista con "cadena de caracteres" en pantalla
        lst es una lista con cadena de caracteres ["A", "e", "I", "o", "U"]
    """
    af.print_box("t")
    for i, option in enumerate(lst):
        af.print_text(f"[{i+1}]>" + option, indent)
    af.print_box("b")





# FUNCIONES UTILES PARA EL RESTO DE OPCIONES
def filtrar_por(user_input:str, option:str):
    """ Filtra series por una opcion de manera lineal:
        title, genre, duration, etc...
    """
    for serie in DATOS["series"]:
        if user_input.lower() == serie[option].lower():
            return True
    return False


def seleccionar_por(user_input:str, option:str):
    """" Retorna una lista con los nombres de series que tienen una opcion en comun. """
    lst = []
    for serie in DATOS["series"]:
        if user_input.lower() == serie[option].lower():
            lst.append(serie)
    return lst
    
    
def obtener_opcion_aleatoria(option="title"): 
    """ Retorna una opcion aleatoria de a la lista json
        option es la opcion que queremos obtener ("titulo, genero, popularidad")
        "title" por default
    """
    return random.choice(DATOS["series"])[option]
    
    
def salir():
    """ Rompe el while loop para cerrar el programa """
    global LOOP
    LOOP = False







# IMPRIMIR FUNCIONALIDAD DE LAS OPCIONES DE LA PANTALLA PRINCIPAL
#1
def buscar_series():
    """ Imprime si la serie ingresada por el usuario esta en la base de datos """
    # HAY QUE DARLE ESTILO A ESTO
    nombre = preguntar_usuario("INGRESE EL NOMBRE DE LA SERIE (en ingles): ")
    
#    print("buscando serie... ")

    if filtrar_por(nombre, "title"):
        imprimir_texto_ensanguchado(f'La serie "{nombre}" SI se encuentra disponible.')
    else:
        imprimir_texto_ensanguchado(f'La serie "{nombre}" NO se encuentra disponible.')

    salir()



#2
def recomendar_relacionado():
    """ Recomienda una serie relacionada a la serie ingresada por el usuario """
    nombre = preguntar_usuario("INGRESE EL NOMBRE UNA SERIE QUE LE GUSTE (en ingles): ")
    print("NO IMPLEMENTADO AUN :(")
    salir()



#3
def recomendar_aleatorio():
    nombre = obtener_opcion_aleatoria()
    print("recomendando serie aleatoria...")
    
    af.print_box("t")
    af.print_text('TE RECOMIENDO QUE MIRES:', "c")
    af.print_text(f'"{nombre}"', "c")
    af.print_text('¡ESTA MUY BUENA!', "c")
    af.print_box("b")
    salir()
    
    
    
#4
def filtrar_por_genero():
    """ Imprime las series del genero ingresado por el usuario """
    print('Ejemplo de generos: "Talk", "Horror", "Comedy", "Crime", etc...')
        
    genero = preguntar_usuario("INGRESE EL NOMBRE DEL GENERO (en ingles): ")
    lst = seleccionar_por(genero, "genre")
    
#    print("filtrando por generos...")
    
    if len(lst) > 0:
        af.print_box("t")
        af.print_text(f'Se encontraron estas series del genero "{genero}"'.upper(), "c",)
        af.print_space("-")
        [af.print_text(f"[{i+1}]>" + serie["title"]) for i, serie in enumerate(lst)]
        af.print_box("b")
    else:
        imprimir_texto_ensanguchado(f'No se encontro el genero "{genero}"'.upper())
    
    salir()



#5
def filtrar_por_temporadas():
    """ Imprime las series que tienen menos o igual cantidad de temporadas
        utilizando el arbol binario
        que la ingresada por el usuario
    """
    
    
    
    print("NO IMPLEMENTADO AUN :(")
    salir()



#6
def filtrar_por_duracion_episodio():
    """ Imprime las series con menos duracion promedio de episodio
        el usuario debe ingresar la duracion promedio de una lista en pantalla
    """
    print("NO IMPLEMENTADO AUN :(")
    salir()



#7
def filtrar_por_edad():
    """ Imprime las peliculas que son aptas para cierto publico
        el usuario ingresa la opcion de edad de una lista en pantalla
    """
    print("NO IMPLEMENTADO AUN :(")
    salir()






# FUNCIONES DE INPUT Y SELECCION
def preguntar_usuario(message="text", type_str=True):
    """ Imprime el mensaje en pantalla para que el usuario vea
    """
    if type_str:
        return input(message)
    return int(input(message))


def seleccionar_opcion(user_input:int, method_call_lst:list):
    """ Dependiendo de lo que el usuario ingrese va a llamar a la opcion correcta 
        method_call_lst es una lista con funciones(sin parentesis) que seran ejecutadas aqui
        segun corresponda.
    """    
    # Solo llama a la funcion si el usuario ingresa un nro mayor que 0 y menor/igual al tamaño de la lista
    if 0 < user_input <= len(method_call_lst):
        method_call_lst[user_input-1]()    
    else:  
        print("ESA NO ES UNA OPCION DE LA LISTA")






def main():   
    # Estas variables y titulos deberian ir cada una dentro de una funcion
    # Variables de los titulos y opciones de cada pantalla
    MENSAJE_PANTALLA_PRINCIPAL = "SELECCIONE UNA OPCION DEL MENU: " # mensaje al usuario #1
    TITULO_PANTALLA_PRINCIPAL = "🎞 SERIESPLAY 🎞"
    # Creamos un diccionario que lo guardamos en una variable con su respectivo NOMBRE_OPTIONS
    # en el cual la "clave" es lo que se imprime en pantalla
    # y el "valor" es la funcion a llamar(sin parentesis, solo el nombre de la funcion)
    OPCIONES_PANTALLA_PRINCIPAL = {"Buscar Series": buscar_series,
                                   "Recomendar Serie Relacionada": recomendar_relacionado, # Implementar mas adelante
                                   "Recomendar Serie Aleatoria": recomendar_aleatorio,
                                   "Filtrar Por Genero": filtrar_por_genero,
                                   "Filtrar Por Cantidad De Temporadas": filtrar_por_temporadas,
                                   "Filtrar Por Duracion De Capitulo": filtrar_por_duracion_episodio,
                                   "Filtrar Por Edad": filtrar_por_edad,
                                   "Salir":salir,
    }       
    
    # Imprime los titulos y las opciones en pantalla
    imprimir_texto_ensanguchado(MENSAJE_PANTALLA_PRINCIPAL) # Imprime el titulo de la pantalla principal 
    imprimir_pantalla_ensanguchada(list(OPCIONES_PANTALLA_PRINCIPAL.keys())) # convierte en "list/lista" las "keys/llaves" del diccionario

    
    # Loop de la funcionalidad basica
    while LOOP:
        # Los mensajes deberian ser dinamicos tambien
        # Si el "user" no es "int" dejar un mensaje y que no se rompa
        user = preguntar_usuario(MENSAJE_PANTALLA_PRINCIPAL, False)
        #Necesita el user_input y los valores de un diccionario con funciones
        seleccionar_opcion(user, list(OPCIONES_PANTALLA_PRINCIPAL.values()))
        
    
    
    
if __name__ == "__main__":
    main()
    
    


