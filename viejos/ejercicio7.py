#Ejercicio 7:
#Dada la siguiente lista:
#[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
#mostrar solo los números pares.
#Javier Sosa

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
pares = []

for elem in numeros:
    if elem % 2 == 0:
        pares.append(elem)

print("Los pares son {}".format(pares))
    