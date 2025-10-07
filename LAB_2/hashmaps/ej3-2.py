''' 
Implementa una función que reciba una lista de estudiantes y sus notas (lista 
de tuplas) y devuelva un diccionario donde cada estudiante es clave y su nota 
es el valor. Haz el mismo ejercicios pero leyendo de un fichero el nombre y la 
nota. Formato: Gonzalo;9.9
'''

class Solution:
    def dict(self, file):
        columnas = []
        my_dict = {}
        try:
            with open(file, "r") as f:
                for linea in f:
                    linea = linea.replace("\n", "")
                    columnas.append(linea.split(";"))
                for tupla in columnas:
                    my_dict[tupla[0]] = float(tupla[1])
                return my_dict
        except Exception as e:
            print(e)
            return None

s = Solution()
assert s.dict("arch.csv") == {"Gonzalo": 9.9, "Jorge": 10}
assert s.dict("hola.csv") == None
assert s.dict("") == None
