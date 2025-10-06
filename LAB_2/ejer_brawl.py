''' 
Escriba una funcion que reciba una lista de enteros y los agrupe 
en diccionario por pares e impares
'''

class Solution:
    def agrupar(self, lista):
        diccionario = {"pares":  [], "impares": []}
        for num in lista:
            if num % 2 == 0:
                diccionario["pares"].append(num)
            else:
                diccionario["impares"].append(num)
        return diccionario
    
s = Solution()
assert s.agrupar([1, 2, 3]) == {"pares": [2], "impares": [1,3]}
        