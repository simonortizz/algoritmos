'''

Ejercicios:
1. Implementar una función sumar_lista(lista) que devuelva la suma total.
2. Crear una función que invierta una lista sin usar [::-1] ni reverse().
3. Verificar si una palabra es palíndromo (ej: 'reconocer', 'neuquén').
4. Crear una clase Libro con titulo, autor, año, y método mostrar_info().
5. Definir clase Rectangulo con métodos para calcular área y perímetro.


'''

# 1. Implementar una función sumar_lista(lista) que devuelva la suma total.

def sumar_lista(lista):

    suma = 0

    for i in lista:
        suma = suma + i
    
    print(suma)


# sumar_lista([1,20,3])

# ---------------------------------------------------------------------------

# 2. Crear una función que invierta una lista sin usar [::-1] ni reverse().

def invertir_lista(lista):
    
    sublista = []

    for i in range(len(lista)):
        sublista.append(lista.pop())

    print(sublista)


# invertir_lista([1,2,3,4,5])

# ---------------------------------------------------------------------------

# 3. Verificar si una palabra es palíndromo (ej: 'reconocer', 'neuquén').

def palindromo(palabra:str):

    lista = []
    lista_copia = []
    subpalabra = []

    for i in (palabra):
        lista.append(i)
        lista_copia.append(i)

    for i in range(len(lista)):
        subpalabra.append(lista.pop())

        if lista_copia[i] != subpalabra[i]:
            return print('No coinciden')
    
    print('Las palabras coinciden')



# palindromo('revolver')

# ---------------------------------------------------------------------------

# 4. Crear una clase Libro con titulo, autor, año, y método mostrar_info().

class Libro:
    
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    
    def mostrar_info(self):
        return print(f'Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.anio}')

libro1 = Libro('Harry Potter', 'JK Rowling', '1995')

# libro1.mostrar_info()

# ---------------------------------------------------------------------------

# 5. Definir clase Rectangulo con métodos para calcular área y perímetro.

class Rectangulo:

    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        area = self.largo * self.ancho
        return print(f'El area del rectangulo es: {area}')
    
    def perimetro(self):
        perimetro = (self.largo*2) + (self.ancho*2)
        return print(f'El perimetro del rectangulo es: {perimetro}')

rect1 = Rectangulo(10, 20)

# rect1.area()
# rect1.perimetro()