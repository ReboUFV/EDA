''' 
Implementa una función que reciba un diccionario de productos y precios, y 
devuelva el producto más caro.
'''

class Solution:
    def expensive(self, diccionario):
        return max(diccionario)

s = Solution()
assert s.expensive({"Piano": 3, "piano": 100}) == "piano"
