cant_pares = 0
cant_impares = 0
suma_positivos = 0
producto_negativo = 1

for i in range(0, 5):
    
    numero = int(input("Ingrese un numero distinto de cero: "))
    
    #b. El menor número ingresado.
    if i == 0 :
        menor_numero = numero
        mayor_par = numero
    elif menor_numero > numero :
        menor_numero = numero
    #a. Cantidad de pares e impares.
    if numero % 2 == 0 :
        cant_pares = cant_pares + 1
        #c. De los pares el mayor número ingresado.
        if i == 0 :
            mayor_par = numero
        elif mayor_par < numero :
            mayor_par = numero
    else:
        cant_impares = cant_impares + 1
    
    
    if numero > 0 :
        #d. Suma de los positivos.
        suma_positivos = suma_positivos + numero
    else :
        #e. Producto de los negativos.
        producto_negativo = producto_negativo * numero

print("Cantidad de pares: " , cant_pares)
print("Cantidad de impares: " , cant_impares)
print("El menor numero ingresado: " , menor_numero)
if mayor_par != 1 :    
    print("El mayor de los pares: ", mayor_par)
else :
    print("No hay pares ingresados")
print("Suma de los positivos: " , suma_positivos)
print("Producto de los negativos: ", producto_negativo)