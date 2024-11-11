#Escribir una función que reciba una muestra de números en una lista y 
#devuelva otra lista con sus valores al cuadrado.
def cuadrados_lista(numeros):
    
    cuadrados = []
    for numero in numeros:
        cuadrados.append(numero ** 2)
    return cuadrados

"""Ahora creamos la lista con los numeros que queremos que los eleve al cuadrado"""
muestra = [1,2,3,4,5,6,7]
resultado = cuadrados_lista(muestra)

print("Lista de valores al cuadrado:", resultado)