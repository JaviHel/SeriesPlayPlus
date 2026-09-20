from ui.carga_de_datos import *
from estructuras.arbol_binario import BST

DATOS = cargar_json("datos/dataset_100.json")
SERIES = DATOS["series"]

COUNTER_BST = 0
COUNTER_SECUENCIAL = 0

title_bst = BST()
genre_bst = BST()
age_rating_bst = BST()

year_bst = BST()
pop_metrics_bst = BST()
episode_average_bst = BST()
seasons_bst = BST()
episodes_bst = BST()

# Carga opciones, que su dato es una string(Cadena de caracteres)
title_bst.load_str(SERIES, "title")
genre_bst.load_str(SERIES, "genre")
age_rating_bst.load_str(SERIES, "age_rating")

# Carga opciones, que su dato es un int(Entero)
year_bst.load_int(SERIES, "year")
pop_metrics_bst.load_int(SERIES, "popularity_metrics")
episode_average_bst.load_int(SERIES, "episode_duration_average")
seasons_bst.load_int(SERIES, "seasons")
episodes_bst.load_int(SERIES, "episodes")






































