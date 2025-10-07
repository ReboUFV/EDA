''' 
Implementa una función que reciba dos listas de strings como parámetros
(una más corta que la otra) y encuentre qué palabra falta en la lista más corta.
'''

class Solution:
    def missing(self, lista1, lista2):
        # Caso base por si l1 tiene mas palabras que l2 
        if len(lista1) >= len(lista2):
            return None
        # Busco los elementos que estan en l2 y no en l1 
        return list(set(lista2) - set(lista1))

s = Solution()

assert s.missing(["hola", "Jorge"], ["hola", "Jorge", "guapo"]) == ["guapo"]
assert s.missing([], []) == None
assert s.missing(["hola", "jorge"], ["hola"]) == None
