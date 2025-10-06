''' 
Implementa una función que reciba un string como parámetro y determine si 
todos sus caracteres son únicos. 
'''

class Solution:
    def is_unique(self, string):
        my_set = set()
        for char in string: # O(n)
            if char not in my_set:
                my_set.add(char)
        if len(my_set) == len(string):
            return True
        else:
            return False

s = Solution()
assert s.is_unique("hola") == True
