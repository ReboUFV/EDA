''' 
Implementa una función que reciba dos listas del mismo tamaño: una con 
claves y otra con valores, y construya un diccionario asociando cada clave 
con su valor. 
'''

class Solution:
    def builder(self, claves, valores):
        my_dict = {}
        if len(claves) != len(valores):
            return None
        for i in range(len(claves)):
            my_dict[claves[i]] = valores[i]
        return my_dict

s = Solution()
assert s.builder(["Jorge", "Maria"], [1,2]) == {"Jorge": 1, "Maria": 2}
assert s.builder([],[]) == {}
assert s.builder([1,2,3], [1,2]) == None

