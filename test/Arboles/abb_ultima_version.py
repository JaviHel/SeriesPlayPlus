# Pedimos el codigo y lo enviaron en mensajes de whatsapp y lo pegamos aqui para ver
# no esta correctamente implementado para ser usado.
# deberia estar en sus respectivos archivos (que no fueron enviados) de manera
# modular.
# por otra parte, no se utilizó porque tiene hardcodeado la opcion de serie que se desea
# utilizar y solo podria utilizarse para una sola opcion.


class Nodo: #Hace los nodos
    def _init_(self, dato=None): #"Dato" es lo que yo voy a pasarle (Nombre, Año, Género)
        self.dato = dato #Se guarda el valor en este nodo
        self.izquierdo = None #Acá se crea el puntero para un nodo vacío para la izquierda
        self.derecho = None #Acá se crea el puntero para un nodo vacío para la derecha.
        
        
        
        
from clasenodo import Nodo

class NodoArbol:
    #Clase nodo árbol"""

    def __init__(self, dato = None):
        self.raiz=None #Le pasamos el primer dato y ese dato pasa a ser la raíz
        if dato is not None:
            self.raiz = Nodo(dato)#Acá se tendría que pasar el dato

    def __agregar_recursivo(self,nodo,dato): #"Agregar_recursivo" está en modo privado. Recorre el árbol.
        if dato['title'] < nodo.dato['title']: #Si el nuevo dato (dato) que ingresa es menor al dato actual (nodo.dato)...
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato) #...Se corre a la izquierda si el nodo está vacío (nodo.izquierdo is None)
            else:
                self.__agregar_recursivo(nodo.izquierdo, dato)#Vuelve a llamar a "Agregar_recursivo" si "nodo.izquierdo" está ocupado para ir de nuevo a la izquierda
        else: #si es mayor se va para la derecha haciendo lo mismo que hizo en la izquierda.
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecho, dato)

#RECORRIDOS INORDEN, PREORDEN Y POSTORDEN

    def __inorden_recursivo(self,nodo,resultado):#Recorre el árbol y ordena todos los valores menores a la izquierda y los mayores a la derecha.
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierdo,resultado) #Va a la izquierda
            resultado.append(nodo.dato)#En esta línea es donde se guarda en la lista "resultado". "Append" se usa para agregar un elemento al final de una lista
            self.__inorden_recursivo(nodo.derecho,resultado) #Va a la derecha

    def __preorden_recursivo(self,nodo, resultado):#Va en el sentido Raiz -> Izquierda -> Derecha
        if nodo is not None:
            resultado.append(nodo.dato)
            self.__preorden_recursivo(nodo.izquierdo, resultado)
            self.__preorden_recursivo(nodo.derecho, resultado)
    
    def __postorden_recursivo(self,nodo,resultado):#Va en el sentido Izquierda -> Derecha -> Raíz
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierdo, resultado)
            self.__postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

#BÚSQUEDA

    def __buscar(self,nodo, busqueda): #Después de que se ordena todo se hace la búsqueda.
        if nodo is None: #Si el dato que busco no está devuelve "None"
            return None 
        if busqueda == nodo.dato['title']: #Si el dato que busco está devuelve el nodo
            return nodo
        elif busqueda < nodo.dato['title']: #Si el dato que busco es menor al nodo busca a la izquierda, sino busca a la derecha.
            return self.__buscar(nodo.izquierdo, busqueda)
        else:
            return self.__buscar(nodo.derecho, busqueda)

    def insertar(self, dato):#Este es el método que uso para agregar un dato
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)#Empieza desde la raiz


    def inorden(self):
        print("Imprimiendo árbol en orden")
        resultado = [] #Esta es la lista vacía que se va llenando con las funciones de inorden, preorden y postorden
        self.__inorden_recursivo(self.raiz,resultado)
        for item in resultado:
            print(item['title']) #Se imprime los elementos ordenados.
        return len(resultado) #Cuenta la cantidad de elementos ordenados

    def preorden(self):
        print("Imprimiendo árbol en preorden")
        resultado = []
        self.__preorden_recursivo(self.raiz,resultado)
        for item in resultado:
            print(item['title']) #Se imprime los elementos ordenados.
        return len(resultado)

    def postorden(self):
        print("Imprimiendo árbol en postorden")
        resultado = []
        self.__postorden_recursivo(self.raiz,resultado)
        for item in resultado:
            print(item['title']) #Se imprime los elementos ordenados.
        return len(resultado)

    def buscar(self, busqueda): #Este es el método que llamo desde "main.py"
        return self.__buscar(self.raiz, busqueda) #Devuelve el resultdo que me da "__buscar"   
        
        
        
        
        
        
        
import json
#from basearbol import NodoArbol

def iniciar_programa():
    with open('dataset_10.json', 'r') as archivo:
        datos_cargados = json.load(archivo)
        elementos = datos_cargados['series']

    raiz = NodoArbol()

    for dato in elementos:
        raiz.insertar(dato) # Creamos la raíz del árbol


    # Mostramos los elementos ordenados (recorrido inorden)
    print("Elementos ordenados:", raiz.inorden())
    print("Elementos en preorden:", raiz.preorden())
    print("Elementos en postorden:", raiz.postorden())

    
if __name__ == '__main__':
    iniciar_programa()

#Al final me devuelve la cantidad de elementos ordenados y el orden en cada uno (inorden, preoden,postorden)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     

