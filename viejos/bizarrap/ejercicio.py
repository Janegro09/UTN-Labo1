from data import lista_bzrp
VACIO = "No hay videos"

def get_max_or_min_by_key(lista, key, operation):

    if(operation == "max"):
        resultado = get_max(lista, key)        
    else:
        resultado = get_min(lista, key)

    return resultado

def get_max(lista, key):
    '''INICIALIZAMOS Y VALIDAMOS LISTA'''
    maximo = validar_lista(lista_bzrp)
    '''RECORREMOS LISTA PARA ENCONTRAR EL MAXIMO'''
    for elem in lista:
        if elem[key] > maximo[key]:
            maximo = elem

    return maximo

def get_min(lista, key):
    '''INICIALIZAMOS Y VALIDAMOS LISTA'''
    minimo = validar_lista(lista_bzrp)
    '''RECORREMOS LISTA PARA ENCONTRAR EL MINIMO'''
    for elem in lista:
        if elem[key] < minimo[key]:
            minimo = elem

    return minimo

def validar_lista(lista):
    '''SI ESTÁ VACIA NO PODEMOS COMPARAR'''
    if len(lista) == 0:
        return VACIO
    else:
        return lista[0]
    
def get_total_by_key(lista, key):
    total = 0
    for elem in lista:
        total = total + elem[key]
    
    return total

def get_promedio(lista):
    cantidad_views = get_total_by_key(lista, "views")

    if cantidad_views == 0:
        return VACIO
    else:
        return cantidad_views / len(lista)

maximo = get_max_or_min_by_key(lista_bzrp, "views", "max")
if(maximo == VACIO):
    print(VACIO)
else:
    print("el video con más reproducciones es {}".format(maximo["title"]))

minimo = get_max_or_min_by_key(lista_bzrp, "views", "min")
if(minimo == VACIO):
   print(VACIO)     
else:
    print("el video con menos reproducciones es {}".format(minimo["title"]))

reproducciones_totales = get_total_by_key(lista_bzrp, "views")
print("reproducciones totales {}".format(reproducciones_totales))

promedio = get_promedio(lista_bzrp)
print("Promedio de vistas {}".format(promedio))

maximo_duracion = get_max_or_min_by_key(lista_bzrp, "length", "max")
if(maximo_duracion == VACIO):
    print(VACIO)
else:
    print("el video con más duracion es {}".format(maximo_duracion["title"]))

minimo_duraciones = get_max_or_min_by_key(lista_bzrp, "length", "min")
if(minimo_duraciones == VACIO):
    print(VACIO)
else:
    print("el video con menos duracion es {}".format(minimo_duraciones["title"]))
