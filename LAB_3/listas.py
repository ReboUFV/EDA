''' 
Apuntes de listas enlazadas
'''
# Estructura de datos lineal que consiste en unos datos y puntero al siguiente nodo

'''
Ejs: Ver si en una lista con valores unicos hay un ciclo
'''


''' 
Métodos
'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, x): # O(n) temp 
        nuevo = Nodo(x)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, posicion):
        if not self.cabeza:
            return

        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
            return
        
        actual = self.cabeza
        indice = 0
        while actual and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1

        if actual and actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente





