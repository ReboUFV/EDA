''' 
Implementa una función que reciba un string y devuelva un diccionario con la 
frecuencia de cada carácter. 
'''

class Solution:
    def freq(self, string):
        tabla = {}
        for char in string:
            try:
                tabla[char] += 1
            except KeyError:
                tabla[char] = 1
        return tabla

s = Solution()
assert s.freq("Solo") == {"S": 1, "o": 2, "l": 1}
assert s.freq("") == {}

