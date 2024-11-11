#Escribir una función que calcule el área de un círculo y otra que calcule
#el volumen de un cilindro usando la primera función.
# Función para calcular el área de un círculo
def area_circulo(radio):
    return 3.1416 * radio**2

"""Función para calcular el volumen de un cilindro"""
def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

"""Pedimos al usuario el radio y la altura"""
radio = float(input("Dime el radio del círculo: "))
altura = float(input("Dime la altura del cilindro: "))

""""Calculamos el área del círculo y el volumen del cilindro"""
area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)

print(f"Área del círculo: {area}")
print(f"Volumen del cilindro: {volumen}")



