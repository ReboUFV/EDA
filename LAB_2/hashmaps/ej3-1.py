''' 
Implementa una función que reciba una lista de estudiantes y sus notas (lista 
de tuplas) y devuelva un diccionario donde cada estudiante es clave y su nota 
es el valor. Haz el mismo ejercicios pero leyendo de un fichero el nombre y la 
nota. Formato: Gonzalo;9.9
'''

class Solution:
    def dict_estd(self, lista):
        my_dict = {}
        for tupla in lista:
            my_dict[tupla[0]] = tupla[1]
        return my_dict

s = Solution()
assert s.dict_estd([("jorge", 3), ("maria", 9)]) == {"jorge": 3, "maria": 9}
assert s.dict_estd([]) == {}

