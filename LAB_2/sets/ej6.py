''' 
Implementa una función que reciba una lista de enteros como parámetro y 
devuelva el primer elemento que aparece más de una vez. 
''' 

class Solution:
    def duplicate(self, lista):
        my_set = set()
        for num in lista: # O(n) 
            if num not in my_set:
                my_set.add(num)
            elif num in my_set:
                return num
        return None

s = Solution()
assert s.duplicate([1,2,2,3,4,4]) == 2
assert s.duplicate([1,2,3,4]) == None

