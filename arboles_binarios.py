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
    Simulación de estructura de directorios.

    
#       A
#      / \ 
#     B   C
#    / \   \   
#   D   E   F

'''

from listas_enlazadas import Lista_enlazada

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


def encontrar_altura(arbol):
    if arbol == None: return 0

    return max(
            encontrar_altura(arbol.izquierda), 
            encontrar_altura(arbol.derecha)
            ) + 1 # -> + 1 es porque se suma la cabeza de ese arbol


# -------------------------------------------------------------------------------------

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

# print(nodos_nivel(arbol, 2))


# -------------------------------------------------------------------------------------

def imprime_nivel(nodo, nivel=0):

    # BEGIN IF
    if nodo is None:
        return 0
    # END IF


    # BEGIN IF
    if nivel == 0:
        print(nodo.carga, end="")
        return
    # END IF

    imprime_nivel(nodo.izquierda, nivel - 1)
    imprime_nivel(nodo.derecha, nivel - 1)


    

# altura = encontrar_altura(arbol)
# for nivel in range(altura):
#     imprime_nivel(arbol, nivel)
#     print()


# -------------------------------------------------------------------------------------

def coincide(raiz, cabeza):

    if raiz == None and cabeza == None:
        return True
    
    def comparar(nodo_arbol, nodo_lista):

        if nodo_arbol == None or nodo_lista == None:
            return False

        if nodo_arbol == None and nodo_lista == None:
            return True
        
        if nodo_arbol.carga != nodo_lista.carga:
            return False
        
        if (nodo_arbol.izquierda == None and nodo_arbol.derecha == None) and nodo_lista.siguiente == None:
            return True
        

        return (comparar(nodo_arbol.izquierda, nodo_lista.siguiente) or 
                comparar(nodo_arbol.derecha, nodo_lista.siguiente))
    
    return comparar(raiz, cabeza)



lista = Lista_enlazada()

# Insertar elementos
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(5)


arbol = Arbol(1,
        Arbol(2,
            Arbol(4),
            Arbol(5)
        ),
        Arbol(3)
    )

# print(coincide(arbol, lista.cabeza))

# -------------------------------------------------------------------------------------

def rama_larga(nodo):
    if nodo is None:
        return []

    rama_izquierda = rama_larga(nodo.izquierda)
    rama_derecha = rama_larga(nodo.derecha)

    if len(rama_izquierda) > len(rama_derecha):
        return [nodo.carga] + rama_izquierda
    else:
        return [nodo.carga] + rama_derecha



arbol = Arbol('A', 
                Arbol('B', 
                        Arbol('D'), 
                        Arbol('E', 
                                None, 
                                Arbol('G'))),
                Arbol('C', 
                        None, 
                        Arbol('F')))
'''
           A
         /   \
        B     C
       / \     \
      D   E     F
           \
            G
'''

# print(rama_larga(arbol))
