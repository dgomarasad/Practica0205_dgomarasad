#Escribir una función que convierta un número decimal en binario y otra
#que convierta un número binario en decimal.
def decimal_a_binario(decimal):
    return bin(decimal)[2:]  


numero_decimal = 21
print(f"El número decimal {numero_decimal} en binario es: {decimal_a_binario(numero_decimal)}")

#Funcion para convertir binario a decimal
def binario_a_decimal(binario):
    return int(binario, 2)  


numero_binario = '10101'
print(f"El número binario {numero_binario} en decimal es: {binario_a_decimal(numero_binario)}")

