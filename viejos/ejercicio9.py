#Ejercicio 9:
#Dadas las siguientes listas:
#edades = [25,36,18,23,45]
#nombre = ["Juan","Ana","Sol","Mario","Sonia"]
#y considerando que la posición en la lista corresponde a la misma persona,
#mostar el nombre de la persona más joven

#Javier Sosa

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

posición_menor = 0
indice = 0
edad_menor = edades[0]

for edad in edades:
    if(edad < edad_menor):
        posición_menor = indice
        edad_menor = edad
    indice = indice + 1

print("el menor es {} con {}".format(nombre[posición_menor], edad_menor))
    