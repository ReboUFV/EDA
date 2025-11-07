# 🌳 Árboles

### Conceptos básicos

- **Hoja** → Nodo sin hijos  
- **Raíz** → Nodo sin padre  
- **Camino** → Secuencia de nodos conectados por aristas desde un nodo origen hasta un nodo destino  
  - Si no repite nodos, se llama *camino simple*.  
- **Ascendiente / Descendiente** → Un nodo es ascendiente de otro si está antes en el camino, y viceversa.

---

### Propiedades

- **Altura de un nodo** → Longitud del camino más largo desde ese nodo hasta una hoja.  
- **Altura de un árbol** → Altura de la raíz.  
- **Profundidad de un nodo** → Longitud del camino desde la raíz hasta ese nodo.  
- **Profundidad de un subárbol** → Profundidad del nodo que actúa como raíz de ese subárbol.  
- **Nivel** → Conjunto de nodos situados a la misma profundidad.  
- **Subárbol** → Árbol formado por un nodo y todos sus descendientes.  
- **Tamaño / Cardinalidad** → Número total de nodos del árbol.  
- **Arista** → Conexión entre dos nodos adyacentes.

---

## 🌲 Recorridos de un árbol binario

Existen **tres maneras principales de recorrer** un árbol binario:

### 1. **Preorder (preorden)**
1. Visita la raíz  
2. Va al subárbol izquierdo  
3. Va al subárbol derecho  

```python
def preorder(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorder(nodo.izquierdo)
        preorder(nodo.derecho)
```

> 🔹 La llamada recursiva continúa bajando por los hijos izquierdos antes de visitar los derechos.  
> 🔹 Cuando termina con los izquierdos, retrocede y continúa con los derechos.

---

### 2. **Inorder (inorden)**
1. Visita el subárbol izquierdo  
2. Visita la raíz  
3. Visita el subárbol derecho  

---

### 3. **Postorder (postorden)**
1. Visita el subárbol izquierdo  
2. Visita el subárbol derecho  
3. Visita la raíz  

---

# ⚙️  Heap (Montículo)

### Definición

Estructura de datos en forma de **árbol binario completo**.

- En un **min-heap**, el valor mínimo siempre está en la raíz.  
- En un **max-heap**, el valor máximo siempre está en la raíz.  
  - Para simularlo con `heapq` (que solo implementa min-heap), se pueden multiplicar los valores por `-1`.

---

### Operaciones y complejidad

| Operación | Descripción | Complejidad |
|------------|--------------|--------------|
| `heappush` | Insertar un elemento | O(log n) |
| `heappop` | Extraer el mínimo | O(log n) |
| `heap[0]` | Ver el mínimo | O(1) |
| `heapify` | Convertir una lista en heap | O(n) |

### Implementación
Esta es una implementación sencilla del TAD heap
```python
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
```

