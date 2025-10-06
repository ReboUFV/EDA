''' 
Implementa una función que reciba dos listas de enteros como parámetros y 
devuelva los elementos que están en una u otra lista, pero no en ambas. 
'''

class Solution:
    def no_intersect(self, list1, list2):
        return list(set(list1) ^ set(list2))

s = Solution()
assert s.no_intersect([1,2,3,4], [1,2,5,7]) == [3,4,5,7]
assert s.no_intersect([], [1,2,5,7]) == [1,2,5,7]
assert s.no_intersect([1,2,3,4], [1,2,3,4]) == []

