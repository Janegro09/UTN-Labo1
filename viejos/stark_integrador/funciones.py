#library
import re

#Constantes
ERROR_1 = "Error: Lista de héroes vacía"

def menu_stark(lista:list):
    lista = normalizar_lista(lista)
    #recibe una lista para trabajar las funciones del menu
    while True:
        opcion = menu_interactivo("elija una opcion\n 1- Imprimir nombres\n 2- Imprimir nombre y altura\n 3- Imprimir el super más alto\n 4- Imprimir el super más bajo \n 5- Imprimir la altura promedio \n 6- Imprimir los super con max y min \n 7- Imprimir los super más y menos pesado \n 8- Salir")

        if opcion == "1":
            print_list_by_key(lista, "nombre")

        if opcion == "2":
            print_list_by_key(lista, "nombre", "altura")

        if opcion == "3":
            maximo = calcular_max_min_dato(lista,"altura", "maximo")
            print(maximo)

        if opcion == "4":
            minimo = calcular_max_min_dato(lista,"altura", "minimo")
            print(minimo)

        if opcion == "5":
            promedio = calcular_promedio(lista, "altura")
            print(promedio)

        if opcion == "6":
            maximo = calcular_max_min_dato(lista,"altura", "maximo")
            minimo = calcular_max_min_dato(lista,"altura", "minimo")
            print("el más alto es {}".format(maximo["nombre"]))
            print("el menos alto es {}".format(minimo["nombre"]))

        if opcion == "7":
            maximo = calcular_max_min_dato(lista,"peso","maximo")
            minimo = calcular_max_min_dato(lista,"peso","minimo")
            print("el más pesado es {}".format(maximo["nombre"]))
            print("el menos pesado es {}".format(minimo["nombre"]))

        if opcion == "8":
            break

def menu_stark_2(lista:list):
    lista = normalizar_lista(lista)
    while True:
        opcion = menu_interactivo("elija una opcion\n 1- Recorrer la lista imprimiendo el nombre de los super M\n 2- Recorrer la lista imprimiendo el nombre de los super F \n 3- Imprimir el super mas alto de genero M\n 4- Imprimir el super mas alto de genero F \n 5- Imprimir el super mas bajo de genero M\n 6- Imprimir el super mas bajo de genero F\n 7- Imprimir el promedio de altura de genero M\n 8- Imprimir el promedio de altura de genero F\n 9- Cuantos y que color de ojos \n 10- Cuantos y que color de pelo \n 11- Cuantos y que tipo de inteligencia \n 0- Salir")

        if opcion == "1":
            lista_m = get_lista_by_key(lista, "genero", "M")
            print_list_by_key(lista_m, "nombre")
        if opcion == "2":
            lista_m = get_lista_by_key(lista, "genero", "F")
            print_list_by_key(lista_m, "nombre")
        if opcion == "3":
            lista_m = get_lista_by_key(lista, "genero", "M")
            maximo_alto_m = calcular_max_min_dato(lista_m, "altura", "maximo")
            print_list_by_key([maximo_alto_m], "nombre")
        if opcion == "4":
            lista_f = get_lista_by_key(lista, "genero", "F")
            maximo_alto_f = calcular_max_min_dato(lista_f, "altura", "maximo")
            print_list_by_key([maximo_alto_f], "nombre")
        if opcion == "5":
            lista_m = get_lista_by_key(lista, "genero", "M")
            minimo_alto_m = calcular_max_min_dato(lista_m, "altura", "minimo")
            print_list_by_key([minimo_alto_m], "nombre")
        if opcion == "6":
            lista_f = get_lista_by_key(lista, "genero", "F")
            minimo_alto_f = calcular_max_min_dato(lista_f, "altura", "minimo")
            print_list_by_key([minimo_alto_f], "nombre")
        if opcion == "7":
            lista_m = get_lista_by_key(lista, "genero", "M")
            promedio_m = calcular_promedio(lista_m, "altura")

            print(promedio_m)
        if opcion == "8":
            lista_f = get_lista_by_key(lista, "genero", "F")
            promedio_f = calcular_promedio(lista_f, "altura")
            print(promedio_f)
        if opcion == "9":
            listar_by_key(lista, "color_ojos")
        if opcion == "10":
            listar_by_key(lista, "color_pelo")
        if opcion == "11":
            listar_by_key(lista, "inteligencia")
        if opcion == "0":
            break

def stark_marvel_app(lista:list):

    lista = normalizar_lista(lista)
    if lista != -1:
        while True:
            mensaje = "Opción inválida"
            opcion= stark_menu_principal()

            if(opcion == 1):
                stark_imprimir_nombres_by_key(lista, "nada")
                mensaje = "Presione enter para continuar"
            if(opcion == 2):
                subopcion = menu_para_keys(lista)
                stark_imprimir_nombres_by_key(lista, subopcion) 
                mensaje = "Presione enter para continuar"
            if(opcion == 3):
                subopcion = menu_para_keys(lista)
                subopcion2 = menu_para_max_min()
                stark_calcular_imprimir_heroe(lista,subopcion,subopcion2)
                mensaje = "Presione enter para continuar"
            if(opcion == 4):
                resultado = stark_calcular_imprimir_promedio_altura(lista)
                print(resultado)
                mensaje = "Presione enter para continuar"
            if(opcion == 0):
                break

            input(mensaje)                

def imprimir_menu(texto:str):
    print(texto)

def menu_para_keys(lista:list)-> int:
#Brinda las keys como opciones para obtener el key para imprimir
    i=0
    total_keys = key_avaibles(lista)
    for i in range(0,len(total_keys)):
        print("{} - {}".format(i+1,total_keys[i]))
        i+=1

    while True:
        opcion = int(input("Ingrese una opcion: "))-1
        if opcion in range(len(total_keys)):
            break
    
    return total_keys[opcion]

def menu_para_max_min()->str:
    while True:
        retorno = input("elija una opcion\n 1- Maximo\n 2- Minimo")
        if retorno == "1":
            retorno = "maximo"
            break
        if retorno == "2":
            retorno = "minimo"
            break
    return retorno

def get_lista_by_key(lista:list, campo:str, filtro:str):
    nueva_lista = []
    for elem in lista:
        if elem[campo] == filtro:
            nueva_lista.append(elem)
    return nueva_lista

def print_list_by_key(lista:list, clave1:str, clave2=False):
    if(clave2):
        for elem in lista:
            texto_clave1 = obtener_by_key(elem, clave1)
            texto_clave1 = obtener_by_key(elem, clave2)
            imprimir_dato(nombre)
            imprimir_dato(nombre)
    else:
        for elem in lista:
            nombre = obtener_by_key(elem, clave1)
            imprimir_dato(nombre)

    input("Presione Enter para continuar...")

def obtener_nombre_y_dato(valor:dict, clave:str, pretexto=""):

    #Imprime los campos que le paso en valor con la clave correspondiente, si mando "nada" solo imprime el nombre
    if clave == "nada" or clave == "nombre" :
        texto = ("Nombre: {0}").format(valor["nombre"])
    else:
        texto = ("{0}Nombre: {1} | {2}: {3}").format(pretexto, valor["nombre"], clave, valor[clave])
    return texto

def imprimir_dato(dato:str):
    print(dato)

#Edicion de dictionary
def key_avaibles(lista:list):
    nueva_lista = list(lista[0].keys())
    return nueva_lista 

def obtener_by_key(dato:dict, clave:str)->str:
    return "{0}: {1}".format(clave, dato[clave])

def validar_lista(lista: list):
    if len(lista) == 0:
        print(ERROR_1)
        lista = -1
    return lista

def normalizar_lista(lista:list):
    dato_normalizado = False

    for elem in lista:
        if not(isinstance(elem["altura"], float)):
            elem["altura"] = float(elem["altura"])
            dato_normalizado = True
        if not(isinstance(elem["peso"], float)):
            elem["peso"] = float(elem["peso"])
            dato_normalizado = True
        if not(isinstance(elem["fuerza"], int)):
            elem["fuerza"] = int(elem["fuerza"])
            dato_normalizado = True
    lista = validar_lista(lista)
    #Valido si la lista está normalizada o 
    if dato_normalizado:
        print("Datos normalizados")


    return lista

def listar_by_key(lista:list, campo:str):
    dic_nuevo = {}
    lista_nueva = armar_lista(lista, campo)
    for elem in lista_nueva:
        dic_nuevo[elem] = len(cant_by_key(lista, campo, elem))
    print(dic_nuevo)
    return

def armar_lista(lista:list, campo:str):
    lista_nueva = []
    for elem in lista:
        if elem[campo] in lista_nueva:
            continue
        else:
            lista_nueva.append(elem[campo])
    return lista_nueva

def cant_by_key(lista:list, campo:str, valor:str):
    #Te arma la cantidad de elementos que posee cada key
    cant = []
    for elem in lista:
        if elem[campo] == valor:
            cant.append(elem)
    return cant

def ordenar_lista(lista:list, tipo:str):
    n = len(lista)
    ordenado = False
    while not ordenado:
        ordenado = True
        if tipo == "mayor":
            for i in range( n - 1 ):
                if(lista[i] > lista[i+1]):
                    aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = aux
                    ordenado = False
        if tipo == "menor":
            for i in range( n - 1 ):
                if(lista[i] < lista[i+1]):
                    aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = aux
                    ordenado = False
    return lista


#Calculos

def calcular_max_min_dato(lista:list, clave:str, tipo:str)->dict:
    max_min = lista[0]
    if tipo == "maximo":
        max_min = calcular_max(lista, clave)
        
    if tipo == "minimo":
        max_min = calcular_min(lista, clave)

    return max_min

def calcular_max(lista:list, clave:str) -> dict:
    max = lista[0]
    for elem in lista:
        if max[clave] < elem[clave]:
            max = elem
    return max

def calcular_min(lista:list, clave:str) -> dict:
    min = lista[0]
    for elem in lista:
        if min[clave] > elem[clave]:
            min = elem
    return min
        
def calcular_promedio(lista:list, valor:str):
    suma = sumar_dato_heroe(lista,valor)
    return dividir(suma, len(lista))

def sumar_dato_heroe(lista:list, valor:str):
    total = 0
    for elem in lista:
        total = total + elem[valor]
    return total

def dividir(dividendo:float, divisor:float)->float:
    retorno = 0
    if(divisor != 0):
        retorno = dividendo / divisor
    return retorno

def validar_entero(numero:str):
    retorno = False
    retorno = re.search('[0-9]+', numero)
    # print(retorno)
    return retorno

#Funciones stark

def stark_imprimir_nombres_by_key(lista:list, clave:str):
#Cumple con la funcionde de stark_imprimir_nombres_heroes
    for elem in lista:
        resultado = obtener_nombre_y_dato(elem,clave)
        imprimir_dato(resultado)

def stark_calcular_imprimir_promedio_altura(lista:list):
    retorno = calcular_promedio(lista, "altura")
    return retorno

def stark_calcular_imprimir_heroe(lista:list, clave:str, max_min:str):
    nombre = calcular_max_min_dato(lista, clave, max_min)
    pretexto = "{} {}: ".format(max_min, clave)
    texto = obtener_nombre_y_dato(nombre, clave, pretexto)
    print(texto)

def stark_menu_principal():

    retorno = -1
    imprimir_menu("elija una opcion\n 1- Imprimir nombres\n 2- Imprimir nombres y otro campo\n 3- imprimir maximo por clave\n 4- imprimir altura promedio\n 0- Salir\n")
    opcion=input("")
    resultado = validar_entero(opcion)
    if resultado:
        retorno = int(opcion)

    return retorno
