''' 
Implementa una función que reciba un diccionario y devuelva otro con las 
claves y valores invertidos (los valores pasan a ser claves).
'''

class Solution:
    def invert(self, dicc):
        my_dict = {}
        for clave, valor in dicc.items():
            my_dict[valor] = clave
        return my_dict

s = Solution()
assert s.invert({"Jorge": 2, "Maria": 9}) == {2: "Jorge", 9: "Maria"}
assert s.invert({}) == {}
