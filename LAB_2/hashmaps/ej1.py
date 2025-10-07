''' 
Implementa una función que reciba una lista de palabras y devuelva un
diccionario con cada palabra como clave y el número de veces que aparece
como valor.
'''

class Solution:
    def freq(self, lista):
        tabla = {}
        for word in lista:
            try:
                tabla[word] += 1
            except KeyError:
                tabla[word] = 1

        return tabla

s = Solution()
assert s.freq(["hola", "hola", "jorge"]) == {"hola": 2, "jorge": 1}
assert s.freq([]) == {}


