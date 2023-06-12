#Ejercicio 6:
#Utilizar For
#Dada la siguiente lista:
#[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
#mostrar el mayor.

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

mayor = numeros[0]
for elem in numeros:
    if mayor < elem:
        mayor = elem

print("el mayor es {}".format(mayor))
