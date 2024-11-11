#Escribir una función que reciba un número entero positivo y devuelva su 
#factorial. Realiza el ejercicio mediante bucles interactivos y mediante 
#una función recursiva.
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

    'Ahora le pedimos '
numero = int(input('Dime un numero entero:'))
print(f"Factorial de {numero} :", factorial_iterativo(numero))
