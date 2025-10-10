''' 
Ej Gonzalo: Dada una lista enlazada con 2n posiciones para un n entero, ve a la posicion n y cambiala con la posicion n+1
'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LinLista:
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

class Solution:
    def contar(self, lista):
        cabeza = lista.cabeza
        while cabeza.siguiente != None:
            print("f")

                





