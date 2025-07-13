'''

Ejercicios:
11. Sumar los elementos de una lista de forma recursiva.
12. Implementar funciones factorial(n) y fibonacci(n).
13. Buscar un valor en una lista enlazada usando recursión.
14. Invertir una cadena recursivamente.
15. Verificar si una lista es palíndromo usando recursión.

'''

from listas_enlazadas import Nodo, Lista_enlazada



class lista(Lista_enlazada):

    def __init__(self):
        super().__init__()
    


    # 11. Sumar los elementos de una lista de forma recursiva.
    def sumar_recursiva(self):
        
        # BEGIN IF
        if self.longitud == 0:
            return 0
        # END IF



        # BEGIN FUNCTION
        def suma(nodo):
            
            # BEGIN IF
            if nodo == None:
                return 0
            # END IF

            return suma(nodo.siguiente) + nodo.carga
        # END FUNCTION


        return suma(self.cabeza)
    


    # 13. Buscar un valor en una lista enlazada usando recursión.
    def buscar_recursivo(self, carga):
        
        # BEGIN IF
        if self.longitud == 0:
            print('La lista está vacia.')
            return
        # END IF
        


        def busca(nodo):

            if nodo == None:
                return False
            
            if nodo.carga == carga:
                print('Elemento encontrado')
                return True
            
            return busca(nodo.siguiente)


        return busca(self.cabeza)




# PRUEBA
# lista1 = lista()
# lista1.insertar_al_final(5)
# lista1.insertar_al_final(10)
# lista1.insertar_al_final(15)

# print(lista1.sumar_recursiva())
# print(lista1.buscar_recursivo(5))

# ------------------------------------------------------------------------------

# 12. Implementar funciones factorial(n) y fibonacci(n).

def factorial(n):
    
    if n == 0:
        return 1
    

    return factorial(n-1) * n


# print(factorial(5))


def fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(6)) # -> fiboncacci(6 - 1) = 5 + fibonacci(6 - 2) = 3
