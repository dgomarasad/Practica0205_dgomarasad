#Escribir una función que reciba una muestra de números en una lista y
#devuelva su media.
def calcular_media(numeros):
    """La definicion nos dice la media de los numeros de la lista
       parametros:
       entrada:lista de numeros que queremso que nos haga la media
       salida:media de la lista de numeros"""
      
    return sum(numeros) / len(numeros)


muestra = [1,2,3,4,5,6,7]
print("La media es:", calcular_media(muestra))
