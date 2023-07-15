"""
2- 
Si el monto total de la compra excede de 500000:
    la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.

Si el monto total de la compra no excede de 500000:
    la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante.

El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito
"""
monto_total = int(input("Ingresa un monto: "))
if monto_total > 500000:
    empresa = monto_total * (55/100)
    banco = monto_total * (30/100)
    credito = monto_total - empresa - banco
    credito = credito * (120/100)
else:
    empresa = monto_total * (70/100)
    credito = monto_total * (30/100)
    credito = credito * (120/100)
    banco = 0
deuda = empresa + banco + credito


print("Monto total:", monto_total)
print("La empresa paga:", empresa)
print("El banco paga:", banco)
print("El credito sera de:", credito)
print("Monto total a pagar (deudas)", deuda)

