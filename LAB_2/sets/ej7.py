''' 
Implementa una función que reciba dos listas como parámetros y compruebe 
si la primera es subconjunto de la segunda. 
'''

class Solution:
    def is_subset(self, lista1, lista2):
        empty = set()
        if set(lista1) == empty and set(lista2) == empty:
            return True
        return (set(lista2) & set(lista1)) != empty and not len(lista1) > len(lista2)  

s = Solution()
assert s.is_subset([1,2,3,4], [1,2]) == False
assert s.is_subset([1,2], [1,2,3,4]) == True
assert s.is_subset([], []) == True
assert s.is_subset([1,2], [5,7]) == False
assert s.is_subset([1,2], [1,2]) == True
