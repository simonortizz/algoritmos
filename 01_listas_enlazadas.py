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
        
        
        if self.cabeza.carga != carga and self.cabeza.siguiente == None:
            print('El elemento no está en la lista.')
            return
        
        
        if self.cabeza.carga == carga and self.cabeza.siguiente == None:
            print('Elemento eliminado')
            nodo_eliminado = self.cabeza
            self.longitud -= 1
            self.cabeza = None
            return nodo_eliminado
        

        nodo = self.cabeza
        anterior = self.cabeza


        if self.cabeza.carga == carga and self.cabeza.siguiente != None:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            print('Elemento eliminado')
            return nodo_eliminado
        

        # BEGIN WHILE
        while nodo:

            if nodo.carga == carga:
                anterior.siguiente = nodo.siguiente
                nodo.siguiente = None
                self.longitud -= 1
                print('Carga eliminada.')
                return nodo
            
            anterior = nodo
            nodo = nodo.siguiente
        # END WHILE

# ---------------------------------------------------------------
