from ui.carga_de_datos import *
from estructuras.arbol_binario import BST

DATOS = cargar_json("datos/dataset_1000.json")
SERIES = DATOS["series"]

COUNTER_SECUENCIAL = 0

title_bst = BST()
title_bst.load_str(SERIES, "title")


# COMPARACION BUSQUEDA BINARIA vs SECUENCIAL
search_title = "Forever"


# Contador de busqueda binaria para misma serie
title_bst.search(search_title)
print("BST: ", title_bst.get_counter()) # le toma


# Contador de busqueda secuencial para misma serie

for serie in SERIES:
    if serie["title"].lower() == search_title:
        break
    else:
        COUNTER_SECUENCIAL += 1

print("SEC: ", COUNTER_SECUENCIAL) # le toma 



# ULTIMA SERIE DE CADA DATASET
# dataset_10 = "Bob's Burgers"
# dataset_100 = "The Americans"
# dataset_1000 = "Forever"



# PARA DATASET_10

# buscar la serie "Bob's Burgers" le tomó:
#    5 pasos al BST
#    10 pasos al secuencial


# PARA DATASET_100

# buscar la serie "The Americans" le tomó:
#   8 pasos al BST
#   100 pasos al secuencial


# PARA DATASET_1000

# buscar la serie "Forever" le tomó:
#    13 pasos al BST
#    1000 pasos al secuencial



# SI ORDENAMOS LOS TITULOS ALFABETICAMENTE ANTES DE CARGARLOS EN EL ARBOL BINARIO
# EL ARBOL BINARIO SE CONVIERTE EN SECUENCIAL PORQUE QUEDA DESBALANCEADO
# Y PIERDE SU VELOCIDAD DE BUSQUEDA.




























