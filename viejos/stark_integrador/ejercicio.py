import json
from funciones import stark_marvel_app

with open('stark_integrador\data_stark.json', 'r') as file:
    objeto = json.loads(file)
    
print(objeto)

with open('stark_integrador\data_stark.json','w') as file:
    
    #json.dump("OBJETO","ARCHIVO o")    

def ordenar_lista():

    lista_nombres = ["Jose", "Mauricio", "Anibal", "Valentina", "Ricardo"]

    for i in range (len(lista_nombres)-1):
        for j in range(i+1,len(lista_nombres)):
            aux = lista_nombres[i]
            lista_nombres[i] = lista_nombres[j]
            lista_nombres[j] = aux

    print(lista_nombres)

ordenar_lista()