'''

Ejercicios:
6. Implementar clase Nodo y ListaEnlazada.
7. Agregar métodos:
● insertar_al_final(valor)
● eliminar(valor)
● buscar(valor)
8. Contar la cantidad de nodos usando recursividad.
9. Devolver el valor máximo almacenado.
10. Imprimir los valores en orden inverso (usando recursividad o pila).


'''

# 6. Implementar clase Nodo y ListaEnlazada.

# 7. Agregar métodos:
# ● insertar_al_final(valor)
# ● eliminar(valor)
# ● buscar(valor)

class Nodo:
    
    def __init__(self, carga = None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente

class Lista_enlazada:

    def __init__(self):
        self.cabeza = None
        self.longitud = 0
    
    def insertar_al_final(self, carga):

        nodo_nuevo = Nodo(carga)

        # BEGIN IF
        if self.cabeza == None:
            self.cabeza = nodo_nuevo
            self.longitud += 1
            print('El nodo es la cabeza y el ultimo.')
            return 
        # END IF

        nodo = self.cabeza

        # BEGIN WHILE
        while nodo:

            if nodo.siguiente == None:
                nodo.siguiente = nodo_nuevo
                self.longitud += 1
                print('El nodo es el ultimo.')
                return 
            
            nodo = nodo.siguiente
        # END WHILE
    
    def eliminar(self, carga):
        if self.cabeza == None:
            print('Lista vacia')
            return 


# ---------------------------------------------------------------
