import pygame
import colores

def crear_enemigo(x,y,ancho,alto,parametro):
    imagen_nave = pygame.image.load(parametro)
    imagen_nave = pygame.transform.scale(imagen_nave,(ancho,alto))

    rect_nave = imagen_nave.get_rect()
    rect_nave.x = x
    rect_nave.y = y

    dict_enemigo = {}
    dict_enemigo["surface"] = imagen_nave
    dict_enemigo["rect"] = rect_nave

    return dict_enemigo

def actualizar_pantalla(lista_enemigos, pantalla):
    for enemigo in lista_enemigos:
        pygame.draw.rect(pantalla, colores.COLOR_MARRON_AVENA, enemigo["rect"])
        pantalla.blit(enemigo["surface"],enemigo["rect"])

def crear_lista_enemigos(cant):
    lista_naves = []
    for i in range(cant):
        lista_naves.append(crear_enemigo(0+(i*80),0,60,60,"galaxia\img\spiked1.PNG"))
    return lista_naves