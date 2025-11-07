''' 
Dada una lista de enteros y un numero k devuelve una lista con aquellos elementos repetidos k veces
'''

class Solution:
    def k_times(self, lista, k):
        my_hash = {}
        retorno = []
        for num in lista:
            try:
                my_hash[num] += 1
            except KeyError:
                my_hash[num] = 1
        for clave, valor in my_hash.items():
            if valor >= k:
                retorno.append(clave)
        return retorno

s = Solution()
assert s.k_times([1,1,1,2,3,3,3,3,3], 3) == [1,3]
