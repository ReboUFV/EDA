''' 
Implementa una función que reciba dos listas de enteros como parámetros y 
devuelva los elementos que están en la primera lista pero no en la segunda.
'''

class Solution:
    def diff(self, list1, list2):
        # El operador - es equivalente a usar el método de diferencia de conjuntos 
        return list(set(list1) - set(list2)) # O(n + m) 

s = Solution()
assert s.diff([1,2,3,4,5], [1,3,5,7,8,9,10]) == [2,4]
assert s.diff([], [1,3,5,7,8,9,10]) == []
assert s.diff([1,2,3,4], [1,2,3,4]) == []

