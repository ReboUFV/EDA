''' 
Implementa una función que reciba una lista de enteros con n números
únicos del 0 al n y devuelva el único que falta
'''

class Solution:
    def encontrar_unico(self, lista):
        lista = set(lista)
        max_val = max(lista) # O(n) 
        set_completo = set(range(max_val + 1))
        return set_completo.difference(lista)
    
s = Solution()
assert s.encontrar_unico([0, 1, 3, 4, 5]) == {2}