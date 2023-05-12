from math import sin, pi, radians
print("\t****************************************************************************************************")
print("""\t   Función del prográma saca el área de un Triángulo a partir de sus lados a y b, con el ángulo B""")
print("\t****************************************************************************************************\n")
print("Los datos dependerán si los quieres en \"centímetros\" presiona \"1\" o si lo prefieres en \"metros\" presiona \"2\".\n")
eleccion = 0
while eleccion != 1 and eleccion != 2:
    eleccion = int(input("Elección: "))
if eleccion == 2:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    if a != 0 and b != 0:
        grados = float(input("Ingrese el valor del ángulo B en grados: "))
        radianes = radians(grados)
        A = 1/2 * a * b * sin(radianes)
        print("\nEl área del triángulo es: {0:.2f} metros cuadrados.".format(A))
    else:
        print("Alguno de los lados proporcionados es 0 entonces el resultado es 0.")
if eleccion == 1:
    if a != 0 and b != 0:
        grados = float(input("Ingrese el valor del ángulo B en grados: "))
        radianes = radians(grados)
        A = 1/2 * a * b * sin(radianes)
        print("\nEl área del triángulo es: {0:.2f} centímetros cuadrados.".format(A))
    else:
        print("Alguno de los lados proporcionados es 0 entonces el resultado es 0.")