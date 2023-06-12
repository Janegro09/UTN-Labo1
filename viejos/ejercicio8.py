#Ejercicio 8:
#Dada la siguiente lista:
#[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
#mostrar el número repetido

#Javier Sosa

numeros = [82, 3, 49, 38, 94, 85, 12, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 8, 48, 78, 29, 58]
repetidos = []

for numero in numeros:
    cantidad_repetidas = 0
    for numero_a_comparar in numeros:
        if numero == numero_a_comparar:
            cantidad_repetidas = cantidad_repetidas + 1
    #Si aparece mas de 1 vez es porque está repetido
    if cantidad_repetidas > 1:
        #Para que no aparezca 2 veces en el arreglo de repetidos consulto si ya está agregado
        if not (numero in repetidos):
            repetidos.append(numero)

if(len(repetidos) > 1):
    print("Los repetidos son {}".format(repetidos))
else:
    print("No hay números repetidos")
    