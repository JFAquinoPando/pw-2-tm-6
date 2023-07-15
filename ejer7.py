"""
7- Existen tres tipos de jubilaciones:
- por edad
- por antigüedad joven
- por antigüedad adulta. 

Las personas para la jubilación por edad deben tener 60 años o más y una antigüedad en su empleo de menos de 25 años.

Las personas para la jubilación por antigüedad joven deben tener menos de 60 años y una antigüedad en su empleo de 25 años o más.

Las personas para antigüedad adulta deben tener 60 años o más y una antigüedad en su empleo de 25 años o más.
"""
edad = int(input("Ingresa la edad: "))
antiguedad = int(input("Ingresa la antiguedad: "))
if ( edad >=  60 and antiguedad < 25):
    print("Jubilacion por edad")
elif ( edad < 60 and antiguedad >= 25):
    print("Jubliacion joven")
elif ( edad >= 60 and antiguedad >= 25):
    print("Jubliacion adulta")
else:
    print("aun no te puedes jubilar")
