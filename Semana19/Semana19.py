#Ejercicios Extra de Análisis de Algoritmos

#1
def manual_add(n):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result

#2
def add_formula(n):
    return number * (number + 1) // 2

#¿Cuál es la complejidad de cada versión?
# La complejidad de la versión manual es O(n)

#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
# Usaría la versión con la fórmula cerrada, ya que es O(1) en lugar de O(n)

#1

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

#2

def binary_search(my_list, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


#¿Cuál es la complejidad de cada algoritmo?
# La complejidad del algoritmo de búsqueda lineal es O(n), ya que en el peor de los casos, 


#¿En qué condiciones conviene usar cada uno?
# El algoritmo de búsqueda lineal es conveniente cuando la lista no está ordenada o cuando 
# el tamaño de la lista es relativamente pequeño.


#¿Qué pasa si la lista no está ordenada?
# Si la lista no está ordenada, no se puede usar el algoritmo de búsqueda binaria
# , ya que este requiere que la lista esté ordenada para funcionar correctamente. En este caso
# , solo se puede usar el algoritmo de búsqueda lineal.


#3

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")



#¿Cuál es la complejidad temporal?
# La complejidad temporal de este algoritmo es O(n2), donde n es el número de claves en el diccionario.

#¿Cuanto dura si hay 1 millón de claves?
# Si hay 1 millón de claves, el algoritmo tardaría aproximadamente 1 billón de operaciones, lo cual sería muy lento.

