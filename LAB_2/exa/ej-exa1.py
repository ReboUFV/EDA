''' 
Dada una lista de numeros enteros y un target entero devuelve los indices de los numeros que sumen el target
Puedes suponer que cada entrada tiene exactamente una solucion y que no se usa el mismo elemento dos veces
Puedes devolver la respuesta en cualquier orden
'''

class Solution:
    def target(self, lista, obj):
        my_hash = {}
        for i in range(len(lista)): # O(n) 
            my_hash[lista[i]] = i
        for clave in my_hash: # O(n) 
            if obj - clave in my_hash: # O(1) 
                return [my_hash[clave], my_hash[obj-clave]]

s = Solution()
assert s.target([1,2,3,4,5,6], 11) == [4,5]

            
