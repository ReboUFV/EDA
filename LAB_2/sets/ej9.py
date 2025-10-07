''' 
Implementa una función que reciba una lista de enteros con n números únicos
del 0 al n y devuelva el único número que falta.
'''

class Solution:
    def missing(self, lista):
        my_set = set()
        for i in range(len(lista) + 1):
            my_set.add(i)
        return list(my_set - set(lista))[0]

s = Solution()
assert s.missing([0,1,2,4]) == 3 
assert s.missing([0]) == 1
assert s.missing([]) == 0 
