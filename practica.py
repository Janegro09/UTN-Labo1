import pygame
import colores

pygame.init()

ALTO_VENTANA = 500
ANCHO_VENTANA = 500
rec_pos = [250,400]
REC_TAM = [50,50]
RADIO = 25
pos_circulo = [0-80,60]
pos_circulo2 = [ANCHO_VENTANA-80*1.25,60]
pos_circulo = [0-80,60]
pos_circulo2 = [0-80*1.5,60]
ventana_principal = pygame.display.set_mode((ALTO_VENTANA,ANCHO_VENTANA))
pygame.display.set_caption("TESTEANDO")

flag_run = True

# TIMER fabrique un evento independiente del usuario que se ejecuta una vez cada mls que le indique
timer_segundo2 = pygame.USEREVENT
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo2,10)
pygame.time.set_timer(timer_segundo,10)
flag_limite = True
flag_limite2 = True


#LEER IMAGEN
imagen_prota = pygame.image.load("galaxia\img\ship.png")
imagen_prota = pygame.transform.scale(imagen_prota,(40,40))
rect_nave = pygame.Rect(250,400,40,40)
# imagen_prota = pygame.transform.scale(imagen_prota,(40,40))


#LEER IMAGEN
crear_enemigo("galaxia\img\spiked1.PNG",)

#CREAMOS TEXTO
fuente = pygame.font.SysFont("Arial",20)
texto = fuente.render("PUNTAJE:", True, colores.COLOR_AMARILLO_ARENA)

while flag_run:

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if (evento.type == pygame.QUIT):
            flag_run = False
        # if evento.type == pygame.MOUSEBUTTONDOWN:
        #     rec_pos = evento.pos
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundo:
                print(evento)
                if(flag_limite):
                    if pos_circulo[0] < ANCHO_VENTANA - RADIO :
                        pos_circulo[0] = pos_circulo[0] + 2
                    else:
                        flag_limite = not(flag_limite)
                        pos_circulo[1] = pos_circulo[1] + 25
                else:
                    if pos_circulo[0] >  RADIO :
                        pos_circulo[0] = pos_circulo[0] - 2
                    else:
                        flag_limite = not(flag_limite)
                        pos_circulo[1] = pos_circulo[1] + 25

            if evento.type == timer_segundo2:
                if(flag_limite2):
                    if pos_circulo2[0] < ANCHO_VENTANA - RADIO :
                        pos_circulo2[0] = pos_circulo2[0] + 1
                    else:
                        flag_limite2 = not(flag_limite2)
                        pos_circulo2[1] = pos_circulo2[1] + 25
                else:
                    if pos_circulo2[0] >  RADIO :
                        pos_circulo2[0] = pos_circulo2[0] - 1
                    else:
                        flag_limite2 = not(flag_limite2)
                        pos_circulo2[1] = pos_circulo2[1] + 25
            

        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_RIGHT] and rec_pos[0] < ANCHO_VENTANA - REC_TAM[0]:
            rec_pos[0] = rec_pos[0] + 5
        if lista_teclas[pygame.K_LEFT] and rec_pos[0] > 0:
            rec_pos[0] = rec_pos[0] - 5
        # if lista_teclas[pygame.K_UP] and rec_pos[1] > 0:
        #     rec_pos[1] = rec_pos[1] - 5
        # if lista_teclas[pygame.K_DOWN] and rec_pos[1] < ALTO_VENTANA - REC_TAM[1]:
        #     rec_pos[1] = rec_pos[1] + 5


    ventana_principal.fill(colores.COLOR_AZUL_MEDIANOCHE)

    pygame.draw.circle(ventana_principal, colores.COLOR_AMARILLO_MOSTAZA,pos_circulo,RADIO)
    pygame.draw.circle(ventana_principal, colores.COLOR_AZUL_ACERO,pos_circulo2,RADIO*1.25)

    ventana_principal.blit(texto,(10,10))

    pygame.draw.rect(ventana_principal, colores.COLOR_ROJO_INDIAN,(250,400,40,40))
    ventana_principal.blit(imagen_prota,rect_nave)
    
    pygame.draw.rect(ventana_principal, colores.COLOR_MARRON_AVENA, rect_nave1)
    ventana_principal.blit(imagen_nave1,rect_nave1)

    pygame.display.flip()

pygame.quit()