''' 
Implementa una función que reciba una lista de enteros como parámetro y
devuelva el número de elementos distintos que contiene.
'''

class Solution:
    def nonequal_counter(self, lista):
        my_set = set()
        cont = 0
        for num in lista:
            if num not in my_set:
                my_set.add(num)
                cont += 1
        return cont

s = Solution()
assert s.nonequal_counter([1,2,1,2,3,4]) == 4
assert s.nonequal_counter([1,2,3]) == 3
assert s.nonequal_counter([]) == 0

