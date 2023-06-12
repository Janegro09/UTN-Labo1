#Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
#distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
#ser soltero.'

edad = int(input("Ingresá una edad: "))
estado_civil = input("Ingresá un estado civil: ")

if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero")