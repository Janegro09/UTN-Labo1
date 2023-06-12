#Ejercicio 10:
#Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
#respectivas listas. Validar el ingreso de datos según su criterio.
#Datos:
#nombre, sexo (f/m), nota (validar).
#Una vez cargados los datos:
#Mostrar el nombre del hombre con nota más baja
#Mostrar el promedio de notas de las mujeres
#Ejemplo:
#nombres = ["Juan","Pedro","Sol","Paco","Ana"]
#sexo = ["m","m","f","m","f"]
#nota = [6,8,10,8,5]

#Javier Sosa

sexo_permitido = ["m", "f"]
notas_permitidas = range(11)
cantidad_alumnos = range(3)
suma_notas = 0
cant_mujeres = 0
bandera_hay_hombres = 0

for i in cantidad_alumnos:
    nombre = input("Ingrese un nombre: ")
    sexo = input("Ingrese un sexo (m o f):")
    while not (sexo in sexo_permitido):
        sexo = input("Ingrese un sexo valido (m o f):")
    
    nota = int(input("ingrese una nota: "))
    while not (nota in notas_permitidas):
        nota = int(input("ingrese una nota valida: "))
    if(sexo == 'f'):
        cant_mujeres = cant_mujeres + 1
        suma_notas = suma_notas + nota
    else:
        if bandera_hay_hombres == 0:
            alumno_menor_nota = nombre
            menor_nota = nota
        else :
            if(menor_nota < nota):
                alumno_menor_nota = nombre
                menor_nota = nota

if cant_mujeres > 0:
    promedio = suma_notas / cant_mujeres
else:
    promedio = "No hay mujeres"

if bandera_hay_hombres == 0:
    alumno_menor_nota = "No hay varones"
print("El mas burro es: {}".format(alumno_menor_nota))
print("El promedio de las mujeres es: {}".format(promedio))