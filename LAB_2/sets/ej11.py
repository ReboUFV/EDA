''' 
 Implementa una función que reciba una lista de enteros como parámetro y
devuelva una lista con todos los elementos que aparecen más de una vez.
'''

class Solution:
    def duplicates(self, lista):
        my_set = set()
        lista_buena = []
        for num in lista:
            if num not in my_set:
                my_set.add(num)
            else:
                lista_buena.append(num)
        return lista_buena
        


s = Solution()
assert s.duplicates([1,1,2,2,3]) == [1,2]
assert s.duplicates([]) == []
assert s.duplicates([1,2,3]) == []


