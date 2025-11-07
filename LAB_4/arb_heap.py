#ARBOLES

'''

Hoja = Nodo sin hijos
Raiz = Nodo sin padre
Camino = Secuencia de nodos conectados por aristas desde un nodoo origen hasta un nodo destino (si no repite nodos es camino simple)
Ascendiente/Descendiente = nodo ascendiente de otro si está antes en camino y vice versa

Altura de un nodo = Longitud del camino mas largo desde ese nodo hasta una hoja
Altura de un arbol = Altura de la raíz
Profundidad de un nodo = Longitud del camino desde la raiz hasta ese nodo
Profundidad de un subarbol = Profundidad del nodo que actua como raiz de ese subarbol
Nivel = Conjunto de nodos situados a la misma profundidad
Subarbol = Arbol formado por un nodo y todos sus descendientes
Tamaño/Cardinalidad = Numero total de nodos del arbol
Arista = Conexión entre dos nodos adyacentes

'''

'''
3 maneras de recorrer:
    - Preorder:
        visita raiz
        Ve al subarbol izquierdo
        ve al subarbol derecho
        
        def preorder(nodo):
            if nodo:
                print(nodo.valor, end=" ")
                preorder(nodo.izquierdo)
                preorder(nodo.derecho)
                
        llamada recursiva que hasta que no se acaben los izquierdos no miran los derechos, luego vuelve al anterior etc
    - Inorder:
        subarbol izq
        raiz
        subarbol derecho
    - Postorder
        subarbol izq
        subarbol derecho
        raiz

'''

#HEAP

'''
Estructura de datos en forma de árbol binario completo
en un min-heap, valor minimo siempre esta en la raiz
En max-heap, valor maximo siempre está en la raíz 
    para esto (de una lista de numeros) se multiplica por -1


Operaciones:
    Insertar (heappush): O(log(n)) -> Siendo n el tamaño del heap
    Extraer mínimo (heappop): O(log(n)) -> Siendo n el tamaño del heap
    Ver mínimo (heap[0]): O(1)
    Convertir lista en heap (heapify): O(n) -> Siendo n el tamaño de la lista

Implementación:

import heapq

h = []
heapq.heappush(h,10)
heapq.heappush(h,5)
heap.heappush(h,8)

print(h)                # [5, 10, 8]
print(heapq.heappop(h)) # 5 

lista = [3, 1, 7, 4, 2]
heapq.heapify(lista)
print(lista)            # [1, 2, 7, 4, 3]

print(lista[0])         # 1 (mínimo)




'''
