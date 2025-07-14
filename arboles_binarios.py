'''

Ejercicios:
Nivel 1:
    Implementar una función no recursiva para recorrer un árbol binario en inorden.
    Función recursiva que cuente la cantidad de nodos de un árbol binario.

Nivel 2:
    Cantidad de nodos en un nivel dado del árbol.

Nivel 3:
    Función que devuelva el recorrido postorden a partir de preorden e inorden.
    Obtener la rama más larga del árbol.

Nivel 4:
    Modelar árbol genealógico con clases Persona y NodoGenealógico.
    Simulación de estructura de directorios.

    
#       A
#      / \ 
#     B   C
#    / \   \   
#   D   E   F

'''

class Nodo:

    def __init__(self, carga = None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente


class Arbol:
    
    def __init__(self, carga, izquierda = None, derecha = None):
        self.carga = carga
        self.izquierda = izquierda
        self.derecha = derecha


    def __str__(self):
        return str(self.carga)



arbol = Arbol('A',
                Arbol('B',
                        Arbol('D'), Arbol('E')), 
                Arbol('C', 
                        None, 
                        Arbol('F')))


def inorden_recursivo(nodo):

    if nodo is None:
        return
    
    inorden_recursivo(nodo.izquierda)
    print(nodo.carga)
    inorden_recursivo(nodo.derecha)

# inorden_recursivo(arbol)


# -------------------------------------------------------------------------------------

def cuenta_nodos_recursivo(nodo):

    if nodo == None:
        return 0
    
    return 1 + cuenta_nodos_recursivo(nodo.izquierda) + cuenta_nodos_recursivo(nodo.derecha)

# print(cuenta_nodos_recursivo(arbol))


# -------------------------------------------------------------------------------------

def nodos_nivel(nodo, nivel=0):

    # BEGIN IF
    if nodo is None:
        return 0
    # END IF


    # BEGIN IF
    if nivel == 0:
        return 1
    # END IF

    return nodos_nivel(nodo.izquierda, nivel - 1) + nodos_nivel(nodo.derecha, nivel - 1)



print(nodos_nivel(arbol, 2))