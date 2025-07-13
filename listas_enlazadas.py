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
class Nodo:
    
    def __init__(self, carga = None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente

class Lista_enlazada:

    def __init__(self):
        self.cabeza = None
        self.longitud = 0



# ● insertar_al_final(valor)
    def insertar_al_final(self, carga):

        nodo_nuevo = Nodo(carga)

        # BEGIN IF
        if self.cabeza == None:
            self.cabeza = nodo_nuevo
            self.longitud += 1
            return 
        # END IF

        nodo = self.cabeza

        # BEGIN WHILE
        while nodo:

            if nodo.siguiente == None:
                nodo.siguiente = nodo_nuevo
                self.longitud += 1
                return 
            
            nodo = nodo.siguiente
        # END WHILE



# ● eliminar(valor)
    def eliminar(self, carga):

        # BEGIN IF
        if self.cabeza == None:
            print('Lista vacia')
            return 
        # END IF
        

        # BEGIN IF
        if self.cabeza.carga != carga and self.cabeza.siguiente == None:
            print('El elemento no está en la lista.')
            return
        #END IF

        
        # BEGIN IF
        if self.cabeza.carga == carga and self.cabeza.siguiente == None:
            print('Elemento eliminado')
            nodo_eliminado = self.cabeza
            self.longitud -= 1
            self.cabeza = None
            return nodo_eliminado
        # END IF


        nodo = self.cabeza
        anterior = self.cabeza


        # BEGIN IF
        if self.cabeza.carga == carga and self.cabeza.siguiente != None:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            print('Elemento eliminado')
            return nodo_eliminado
        # END IF


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
    


# ● buscar(valor)
    def buscar(self, carga):

        # BEGIN IF
        if self.longitud == 0:
            print('La lista está vacia.')
            return
        # END IF
        

        # BEGIN IF
        if self.cabeza.carga == carga:
            print('El elemento existe y es la cabeza.')
            return
        # END IF


        nodo = self.cabeza


        # BEGIN WHILE
        while nodo:
            
            if nodo.carga == carga and nodo.siguiente == None:
                print('El elemento existe y es el ultimo.')
                return
            
            if nodo.carga == carga and nodo.siguiente != None:
                print('El elemento existe y está en el medio.')
                return
            
            nodo = nodo.siguiente
        # END WHILE
        
        print('El elemento no existe en la lista.')
        return



# 8. Contar la cantidad de nodos usando recursividad.
    def cuenta_nodos_recursivo(self):
        
        # BEGIN IF
        if self.longitud == 0:
            print('Lista vacía')
            return 0
        # END IF


        # BEGIN FUNCTION
        def cuenta(nodo):
            
            if nodo == None:
                return 0
            
            return cuenta(nodo.siguiente) + 1
        # END FUNCTION


        return cuenta(self.cabeza)



# 9. Devolver el valor máximo almacenado.
    def maximo_almacenado(self):
        
        # BEGIN IF
        if self.longitud == 0:
            print('Lista vacia')
            return
        # END IF


        # BEGIN IF
        if self.cabeza.siguiente == None:
            return self.cabeza
        # END IF

        
        nodo = self.cabeza
        mayor = self.cabeza.carga

        
        # BEGIN WHILE
        while nodo:

            if nodo.carga > mayor:
                mayor = nodo.carga
            
            nodo = nodo.siguiente
        # END WHILE

        return mayor



# 10. Imprimir los valores en orden inverso (usando recursividad).
    def imprimir_inverso_recursivo(self):
        
        # BEGIN IF
        if self.longitud == 0:
            print('Lista vacia')
            return
        # END IF


        nodo = self.cabeza

        def recursividad(nodo):
            
            if nodo == None:
                return 0
            
            recursividad(nodo.siguiente)
            print(nodo.carga)
        

        return recursividad(nodo)



lista = Lista_enlazada()

# # Insertar elementos
# lista.insertar_al_final(3)
# lista.insertar_al_final(7)
# lista.insertar_al_final(2)
# lista.insertar_al_final(9)
# lista.insertar_al_final(5)

# print("---- PRUEBA DE MÉTODOS ----")

# # 1. Buscar elementos
# print("Buscar 7:")
# lista.buscar(7)  # Debe indicar que existe y está en el medio

# print("Buscar 10:")
# lista.buscar(10)  # Debe indicar que no existe

# # 2. Contar nodos recursivamente
# print("Cantidad de nodos:", lista.cuenta_nodos_recursivo())  # Debe ser 5

# # 3. Valor máximo almacenado
# print("Valor máximo:", lista.maximo_almacenado())  # Debe ser 9

# # 4. Imprimir inverso recursivamente
# print("Imprimir lista en orden inverso:")
# lista.imprimir_inverso_recursivo()
# # Debe imprimir: 5, 9, 2, 7, 3 (cada uno en una línea)

# # 5. Eliminar un elemento y probar si se actualiza
# print("Eliminar elemento 2:")
# lista.eliminar(2)  # Debe indicar que se eliminó

# print("Cantidad de nodos después de eliminar:", lista.cuenta_nodos_recursivo())  # Debe ser 4

# print("Buscar 2 después de eliminar:")
# lista.buscar(2)  # Debe indicar que no existe

# print("Imprimir lista en orden inverso después de eliminar 2:")
# lista.imprimir_inverso_recursivo()
# # Debe imprimir: 5, 9, 7, 3

