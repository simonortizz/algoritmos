'''

16. Implementar una pila (Pila) usando listas o nodos.
17. Usar la pila para invertir una cadena o lista.
18. Validar paréntesis balanceados con pila (ej: "(())()", "((").
19. Implementar una cola circular (Cola) básica.
20. Simular atención por turnos en una cola (agregar y quitar elementos FIFO)

Pila -> FLIFO (Last In First Out) Ejemplo: platos apilados, ultimo agregado, primero en agarrar.
Cola -> FIFO (First In First Out) Ejemplo: cola de supermercado, primero que llega, primero que paga.

Pila
    [3]
    [2]
    [1]

Cola
    [1][2][3]
'''

# 16. Implementar una pila (Pila) usando listas o nodos.
class Pila:
    
    def __init__(self):
        self.elementos = []


    def apilar(self, elemento):
        self.elementos.append(elemento)


    def desapilar(self):
        return self.elementos.pop()


    def isEmpty(self):
        return self.elementos == []



# 17. Usar la pila para invertir una cadena.
def invertir_cadena(cadena):

    pila = Pila()

    for i in cadena:
        pila.apilar(i)
    
    resultado = []

    while not pila.isEmpty():
        resultado.append(pila.desapilar())
    
    return ''.join(resultado)
    

    
cadena = 'Lionel Messi'

# print(invertir_cadena(cadena)) # isseM lenoiL

# -------------------------------------------------------------------------------------

# 18. Validar paréntesis balanceados con pila (ej: "(())()", "((").
def validar_parentisis(cadena):
    
    pila = Pila()

    # BEGIN FOR
    for i in cadena:
        if i == '(':
            pila.apilar(i)
        elif i == ')' and not pila.isEmpty():
            pila.desapilar()
        else:
            return 'Cadena no valida.'
    # END FOR

    # BEGIN IF
    if pila.isEmpty():
        return 'Cadena de parentesis valida.'
    else:
        return 'Cadena no valida.'
    # END IF

cadena = '((()()))' # -> valida
cadena = '(()())))))' # -> no valida


# print(validar_parentisis(cadena))

# -------------------------------------------------------------------------------------


# 19. Implementar una cola (Cola) básica.
class Cola:
    
    def __init__(self):
        self.elementos = []
    

    def encolar(self, elemento):
        self.elementos.append(elemento)


    def desencolar(self):
        return self.elementos.pop(0)
    

    def cantidad(self):
        return len(self.elementos)

    
    def isEmpty(self):
        return self.elementos == []

# -------------------------------------------------------------------------------------

# 20. Simular atención por turnos en una cola (agregar y quitar elementos FIFO)
def simulador_turnos():

    cola = Cola()

    opcion = input('Ingrese 1-paciente/2-atendido/3-salir: ')

    while opcion != '3':


        # BEGIN IF
        if opcion == '1':

            paciente = input('Ingrese paciente: ')
            
            cola.encolar(paciente)

            opcion = input('Ingrese 1-paciente/2-atender/3-salir: ')

        elif opcion == '2' and not cola.isEmpty():

            atendido = cola.desencolar()
            print(f'Paciente atendido: {atendido}')
            print(f'Pacientes esperando: {cola.cantidad()}.')

            opcion = input('Ingrese 1-paciente/2-atendido/3-salir: ')
        else:

            print('No hay paciente para atender.')

            opcion = input('Ingrese 1-paciente/2-atendido/3-salir: ')
        # END IF


# simulador_turnos()