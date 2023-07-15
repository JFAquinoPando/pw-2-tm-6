"""
Leer los tres lados de un triángulo escaleno. Calcular su perímetro
"""

lado1 = int(input("Lado 1:"))
lado2 = int(input("Lado 2:"))
lado3 = int(input("Lado 3:"))

perimetro = lado1 + lado2 + lado3
promedio = (lado1 + lado2 + lado3) / 3

print("El perimetro es:", perimetro)
print("El promedio es:", promedio)
