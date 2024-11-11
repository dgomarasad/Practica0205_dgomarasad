#Escribir una función que reciba una muestra de números en una lista y
#devuelva su media.
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

"""Ahora creamos la lista con """
muestra = [1,2,3,4,5,6,7]
print("La media es:", calcular_media(muestra))
