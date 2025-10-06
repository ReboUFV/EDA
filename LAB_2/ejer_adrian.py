''' 
Implementa una funcion que reciba un diccionario cuya clave
es un producto y el valor es el precio
'''

class Solution:
    def mas_caro(self, dicc):
        precio_max = 0
        producto_max = ""
        for clave, valor in dicc.items(): # O(n) 
            if valor > precio_max:
                precio_max = valor
                producto_max = clave
                
        return producto_max

s = Solution()
assert s.mas_caro({"flauta": 2, "piano": 200000}) == "piano"

            