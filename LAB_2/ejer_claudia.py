''' 
Escriba una funcion que reciba una palabra y devolver la
letra que mas se repita
'''

class Solution:
    def repeticiones(self, palabra):
        dicc = {}
        num_max = 0
        letra_max = ""

        for letra in palabra:
            if letra in dicc:
                dicc[letra] += 1
            else:
                dicc[letra] = 0
     
        for letr, num in dicc.items():
            if num > num_max:
                num_max = num
                letra_max = letr
        
        return letra_max

s = Solution()
assert s.repeticiones("mequetrefe") == "e"
assert s.repeticiones("ooaa") == "o"

