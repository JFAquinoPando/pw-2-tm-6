"""
Si la bolilla es de color blanco no se hará descuento alguno, 
si es verde se le hará un 10% de descuento, 
si es amarilla un 25%, 
si es azul un 50% y 
si es roja un 100%. Determinar 

la cantidad final que el cliente deberá pagar por su compra. Se sabe que sólo hay bolillas de los colores mencionados.
"""
cuenta = 1000000
bolilla = input("Color de bolilla (blanco, verde, amarillo, azul o rojo): ")
descuento = 0
if bolilla == "blanco":
    descuento = 0
elif bolilla == "verde":
    descuento = 10
elif bolilla == "amarillo":
    descuento = 25
elif bolilla == "azul":
    descuento = 50
elif bolilla == "rojo":
    descuento = 100
else:
    print("no existe tu bolilla")

a_pagar = cuenta * (1 - (descuento/100))
print("Total compra:", cuenta)
print("Bolilla: ", bolilla)
print("Descuento:", descuento)
print("A pagar por compra", a_pagar)
