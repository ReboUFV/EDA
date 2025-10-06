''' 
Implementa una funcipon que reciba una lista de palabras y devuelva
un diccionario con cada palabra como clave y el numero de veces
que aparece como valor
''' 

class Solution:
    def contar_letras(self, palabra):
        # Con {} definimos un diccionario vacío 
        freq = {}
         
        for letra in palabra:
            # Si la letra esta en el dicc, añadimos uno (repeticion) 
            if letra in freq:
                freq[letra] += 1
            # Si no esta, la añadimos 
            else:
                freq[letra] = 1
            return freq    
            