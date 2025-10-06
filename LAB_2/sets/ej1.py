''' 
Implementa una función que reciba una lista de enteros como parámetro y 
devuelva una nueva lista sin duplicados.
'''

class Solution:
    def no_duplicates(self, lista):
        my_set = set()
        for num in lista: # O(n) 
            if num not in my_set:
                my_set.add(num)
        # La función list() evaluada en un set convierte un set a una lista
        return list(my_set) # list() es O(n)   

s = Solution()
assert s.no_duplicates([1,2,3,4,4]) == [1,2,3,4]
assert s.no_duplicates([1,2,3,4]) == [1,2,3,4]
assert s.no_duplicates([1,1,1,1,1,1]) == [1]
assert s.no_duplicates([]) == []

