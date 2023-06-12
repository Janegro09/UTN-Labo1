#library
import re
import json

#Constantes
ERROR_1 = "Error: Lista de star wars vacía"
MENSAJE_EXPORTACION = "Exporación realizada"

def convertir_lista(ruta:str, modo:str) -> list:
    with open(ruta,modo) as archivo:
        objeto = json.load(archivo)["results"]
    return objeto

def star_wars_app(lista:list):
    lista = normalizar_lista(lista)
    opcion_anterior=[]
    if lista != -1:
        while True:
            mensaje = "Opción inválida"
            opcion= star_wars_menu_principal()

            if(opcion == 1):
                opcion_anterior = star_wars_calcular_personajes_ordenados_por_key(lista, "height")
                mensaje = "Presione enter para continuar"
            if(opcion == 2):
                opcion_anterior = star_wars_calcular_personajes_max_min_por_key(lista, "gender", "height", "maximo")
                mensaje = "Presione enter para continuar"
            if(opcion == 3):
                opcion_anterior = star_wars_calcular_personajes_ordenados_por_key(lista, "mass")
                mensaje = "Presione enter para continuar"
            if(opcion == 4):
                opcion_anterior = star_wars_buscador(lista)
                mensaje = "Presione enter para continuar"
            if(opcion == 5):
                mensaje = star_wars_exportacion(opcion_anterior, 'parcial\datos.csv')
              
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

def menu_para_max_min(opcion1:str, opcion2:str)->str:
    while True:
        retorno = input("elija una opcion\n 1- {}\n 2- {}".format(opcion1, opcion2))
        if retorno == "1":
            retorno = opcion1
            break
        if retorno == "2":
            retorno = opcion2
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

def obtener_nombre_y_dato(valor:dict, clave:str):
    clave_traducida = traducir_clave(clave)
    #Imprime los campos que le paso en valor con la clave correspondiente, si mando "nada" solo imprime el nombre
    if clave == "nada" or clave_traducida == "Nombre" :
        texto = ("{0}: {1}").format(clave_traducida, valor["name"])
    else:
        texto = ("Nombre: {0} | {1}: {2}").format(valor["name"], clave_traducida, valor[clave])
    return texto

def imprimir_dato(dato:str):
    print(dato)

def traducir_clave(clave:str)->str:
    retorno=""
    if clave=="name":
        retorno = "Nombre"
    if clave=="height":
        retorno = "Altura"
    if clave=="mass":
        retorno = "Peso"
    if clave=="gender":
        retorno = "Genero"
    return retorno

#Edicion de keys
def key_avaibles(lista:list):
    nueva_lista = list(lista[0].keys())
    return nueva_lista 

def obtener_by_key(dato:dict, clave:str)->str:
    return "{0}: {1}".format(clave, dato[clave])

def listar_by_key(lista:list, campo:str):
    dic_nuevo = {}
    lista_nueva = armar_lista_segun_key(lista, campo)
    for elem in lista_nueva:
        dic_nuevo[elem] = len(cant_by_key(lista, campo, elem))
    print(dic_nuevo)
    return

def cant_by_key(lista:list, campo:str, valor:str):
    #Te arma la cantidad de elementos que posee cada key
    cant = []
    for elem in lista:
        if elem[campo] == valor:
            cant.append(elem)
    return cant

#Edicion de listas

def validar_lista(lista: list):
    if len(lista) == 0:
        print(ERROR_1)
        lista = -1
    return lista

def normalizar_lista(lista_original:list) -> list:
    dato_normalizado = False
    #shallow  copy
    lista = lista_original.copy()

    for elem in lista:
        if not(isinstance(elem["height"], int)):
            elem["height"] = int(elem["height"])
            dato_normalizado = True
        if not(isinstance(elem["mass"], int)):
            elem["mass"] = int(elem["mass"])
            dato_normalizado = True
    lista = validar_lista(lista)

    if dato_normalizado:
        print("Datos normalizados")
    else:
        print("Lista ya normalizada")

    return lista

def armar_lista_segun_key(lista:list, campo:str):
    lista_nueva = []
    for elem in lista:
        if elem[campo] in lista_nueva:
            continue
        else:
            lista_nueva.append(elem[campo])
    return lista_nueva

def ordenar_lista(lista:list, tipo:str, clave:str):
    n = len(lista)
    ordenado = False
    while not ordenado:
        ordenado = True
        if tipo == "Ascendente":
            for i in range( n - 1 ):
                if(lista[i][clave] < lista[i+1][clave]):
                    aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = aux
                    ordenado = False
        if tipo == "Descendente":
            for i in range( n - 1 ):
                if(lista[i][clave] > lista[i+1][clave]):
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
    coincide = re.search('^[0-5]$', numero)
    retorno = -1
    if(coincide):
        retorno = int(numero)

    return retorno

#Archivos
def star_wars_exportar_de_resultados(lista:list, nombre_archivo:str)->str:
    datos = []
    for elem in lista:
        #Armo el diccionario uso REGEX
        dic={}
        separacion = re.split('\|',elem)
        dic["Nombre"] = re.split("Nombre: ",separacion[0])[1]
        resto = re.split(": ",separacion[1])
        segunda_key = resto[0]
        dic[segunda_key] = resto[1]
        datos.append(dic)

    with open(nombre_archivo, 'w') as archivo_csv:
        #Escribo los encabezados
        encabezados = ["Nombre",segunda_key]
        archivo_csv.write(','.join(encabezados)+'\n')

        # Escribo en el csv
        for dato in datos:
            fila = [dato["Nombre"], dato[segunda_key]]
            archivo_csv.write(','.join(fila)+'\n')
    return MENSAJE_EXPORTACION

def star_wars_exportar(lista:list, nombre_archivo:str):
    with open(nombre_archivo, 'w') as archivo_csv:
    #     #Escribo los encabezados
        encabezados = key_avaibles(lista)
        archivo_csv.write(','.join(encabezados)+'\n')
        for dato in lista:
            only_values = []
            for encabezado in encabezados:
                only_values.append(str(dato[encabezado]))
            archivo_csv.write(','.join(only_values)+'\n')
    return MENSAJE_EXPORTACION
#Funciones star_wars
def star_wars_calcular_personajes_ordenados_por_key(lista:list, valor:str):
    sub_opcion = menu_para_max_min("Ascendente", "Descendente")
    lista = ordenar_lista(lista, sub_opcion, valor)
    lista_nueva = star_wars_imprimir_nombres_by_key(lista,valor)

    return lista_nueva

def star_wars_calcular_personajes_altura_genero(lista:list):
    sub_opcion = menu_para_max_min("Ascendente", "Descendente")
    lista = ordenar_lista(lista, sub_opcion, "height")
    lista_nueva = star_wars_imprimir_nombres_by_key(lista,"height")

    return lista_nueva

def star_wars_menu_principal() -> int:

    imprimir_menu("elija una opcion\n 1- Listar los personajes ordenados por altura\n 2- Imprimir el personaje más alto de cada genero\n 3- Listar los presonajes ordenados por peso\n 4- Ingresar al buscador de personajes\n 5- Exportar a CSV\n 0- Salir\n")
    opcion=input("")
    retorno = validar_entero(opcion)

    return retorno

def star_wars_imprimir_nombres_by_key(lista:list, clave:str)->list:
#Cumple con la funcionde de star_wars_imprimir_nombres_heroes
    lista_nueva = []
    for elem in lista:
        resultado = obtener_nombre_y_dato(elem,clave)
        imprimir_dato(resultado)
        lista_nueva.append(resultado)
    return lista_nueva

def star_wars_calcular_personajes_max_min_por_key(lista:list, valor1:str, valor2:str, opcion:str)->list:
    sub_lista = []
    clave_traducida = traducir_clave(valor1)
    
    #Calcular sub listas para generos
    total_generos = armar_lista_segun_key(lista, valor1)
    #calcular maximo de cada uno

    for elem in total_generos:
        print("{}: {}".format(clave_traducida, elem))
        sub_lista_generos = get_lista_by_key(lista,valor1,elem)
        maximo = calcular_max_min_dato(sub_lista_generos, valor2, opcion)
        texto = obtener_nombre_y_dato(maximo,valor2)
        print(texto)
        print("*************")
        #pushearlos en una lista para la exportacion
        sub_lista.append(texto)
    return sub_lista

def star_wars_buscador(lista:list)->list:
    resultados = []
    buscar = (input("Ingresa una palabra: ").upper())
    for elem in lista:
        parsea_string = json.dumps(elem).upper()
        resultado = re.findall(buscar,parsea_string)
        if len(resultado) > 0:
            resultados.append(elem)
    #Imprimo los resultados posibles
    print(resultados)
    return resultados

def star_wars_exportacion(lista:list, nombre_archivo:str)->str:
    #Aviso si está vacia o no
    if(len(lista) != 0):
        #Valido para identificar si es resultado del buscador o de un dato puntual
        con_detalle = type(lista[0]) == dict
        if con_detalle:
            mensaje = star_wars_exportar(lista, nombre_archivo)
        else:
            mensaje = star_wars_exportar_de_resultados(lista, nombre_archivo)
    else:
        mensaje = "Primero debes elegir una opción(1-4) que traiga resultados para realizar la exportación"

    return mensaje

#Otras
def star_wars_calcular_imprimir_heroe(lista:list, clave:str, max_min:str):
    nombre = calcular_max_min_dato(lista, clave, max_min)
    texto = obtener_nombre_y_dato(nombre, clave)
    print(texto)

def star_wars_calcular_imprimir_promedio_altura(lista:list):
    retorno = calcular_promedio(lista, "altura")
    return retorno


