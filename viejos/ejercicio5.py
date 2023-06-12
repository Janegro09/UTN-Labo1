precio = 15000
estaciones = ["verano", "otoño", "invierno", "primavera"]
destinos = ["Bariloche", "Mar del Plata", "Cataratas", "Córdoba"]

estacion_elegida = input("Ingrese una estación: ")
while not (estacion_elegida in estaciones) :
    estacion_elegida = input("Ingrese una estación (verano, invierno, otoño, primavera): ")
    
destino_elegido = input("Ingrese un destino: ")
while not (destino_elegido in destinos) :
    destino_elegido = input("Ingrese un destino (Bariloche, mar del plata, cordoba o cataratas): ")

if estacion_elegida == "invierno" :
    if destino_elegido == "Bariloche" :
        precio_final = precio * 1.2
    elif destino_elegido == "Cataratas" or destino_elegido == "Córdoba" :
        precio_final = precio * 0.9
    else :
        precio_final = precio * 0.8

elif estacion_elegida == "verano" :
    if destino_elegido == "Bariloche" :
        precio_final = precio * 0.8
    elif destino_elegido == "Cataratas" or destino_elegido == "Córdoba" :
        precio_final = precio * 1.1
    else :
        precio_final = precio * 1.2

else :
    if destino_elegido == "Córdoba" :
        precio_final = precio
    else :
        precio_final = precio * 1.1

print("Precio final para " + destino_elegido + " en " + estacion_elegida + " es " + str(precio_final))
