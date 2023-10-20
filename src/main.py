import pygame
from sys import exit
from config import *
from funciones_calculo import *
from funciones_dibujo import *
from datos_figuras import figuras
from colisiones import *
 

#inicializar los modulos
pygame.init()
clock = pygame.time.Clock()

# Configuracion pantalla
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Figuras Geométricas")

is_running = True

imagen = pygame.image.load("img/fondo.jpg")
fondo = pygame.transform.scale(imagen,screen_size)
lista_cuadrados = []
tipo = None
imagen = pygame.image.load("img/cierre.jpg")
cierre = pygame.transform.scale(imagen,(40,40))
rect = cierre.get_rect()
rect.topright = (780,20)

while is_running:
    clock.tick(FPS)
    # Detectamos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if tipo == None:
                for cuadrado in lista_cuadrados:
                    if punto_en_rectangulo((x,y),cuadrado["rect"]):
                        tipo = cuadrado["tipo"]
            elif punto_en_rectangulo((x,y),rect):
                tipo = None
                
        
    #-----> Actualizar los elementos
    for figura in figuras:
        if figura["tipo"] == tipo:
            figura_a_dibujar = figura
    
    
    
    #----> Actualizar pantalla
    screen.blit(fondo,(0,0))
    if tipo != None:
        gestionar_calculo_y_grafica(screen,figura_a_dibujar,cierre,rect)
    else:
        lista_cuadrados = dibujar_menu(screen,screen_w_mid,screen_h_mid)
    
   
    pygame.display.flip()
    
pygame.quit()
    
    
        