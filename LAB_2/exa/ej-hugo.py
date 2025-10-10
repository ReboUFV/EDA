''' 
Implementa una función llamada categorizar_unicos que reciba una lista de nombres completos (strings) y devuelva un diccionario donde:
La clave es la letra inicial del nombre (en mayúscula).
El valor es un conjunto (set) que contiene todos los nombres que comienzan con esa letra.
'''

class Solution:
    def categorizar_unicos(self, lista):
        unicos = {}
        emptys = set()
        for element in lista:
            # Convierte el primer carácter en mayuscula y el resto en minuscula
            element = element.capitalize()

            try:
                unicos[element[0]].add(element)

            except KeyError:
                unicos[element[0]] = {element}

            '''
            if unicos == {}:
                unicos[element[0]] = {element}
            else:
                unicos[element[0]].add(element)
                '''
        return unicos

s = Solution()
print(s.categorizar_unicos(["jorge", "juan", "paco"]))
assert s.categorizar_unicos(["jorge", "juan", "paco"]) == {"J": {"Jorge", "Juan"}, "P": {"Paco"}}

