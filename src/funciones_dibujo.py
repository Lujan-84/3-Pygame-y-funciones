import pygame
from config import *
from funciones_calculo import *


def dibujar_rectangulo(screen,figura:dict):
    """Dibuja un rectángulo en la pantalla recibida por parámetro y con las caracteristicas recibidas en un diccionario tambien como parámetro.

    Args:
        screen (): La superficie donde se dibujara el rectangulo
        figura (dict): El diccionario que contiene las caracteristicas de la figura; tipo, dimensiones, posicion inicial y color.
    """
    x,y = figura["posicion_inicial"]
    a,b = figura["dimensiones"]
    pygame.draw.rect(screen,figura["color"],(x,y,a,b))
    
def dibujar_cuadrado(screen,figura:dict):
    """Dibuja un cuadrado en la pantalla recibida por parámetro y con las caracteristicas recibidas en un diccionario tambien como parametro.

    Args:
        screen (): La superficie donde se dibujara el cuadrado
        figura (dict): El diccionario que contiene las caracteristicas de la figura; tipo, dimensiones, posicion inicial y color.
    """
    lado = figura["dimensiones"]
    x,y = figura["posicion_inicial"]
    pygame.draw.rect(screen,figura["color"],(x,y,lado,lado))
    
def dibujar_circulo(screen,figura:dict):
    """Dibuja un círculo en la pantalla recibida por parámetro y con las características recibidas en un diccionario tambien como parámetro.

    Args:
        screen (): La superficie donde se dibujará el círculo
        figura (dict): El diccionario que contiene las caracteristicas de la figura; tipo, dimensiones, posicion inicial y color.
    """    
    radio = figura["dimensiones"]
    x,y = figura["posicion_inicial"]
    pygame.draw.circle(screen,figura["color"],(x,y),radio)
    
def dibujar_triangulo(screen,figura:dict):
    """Dibuja un triángulo en la superficie recibida por parametro y con las caracteristicas recibidas en un diccionario también como parámetro.

    Args:
        screen (): La superficie donde se dibujara el triangulo
        figura (dict): El diccionario que contiene las caracteristicas de la figura; tipo, dimensiones, posicion inicial y color.
    """
    A,B,C = figura["posicion_inicial"]
    pygame.draw.polygon(screen,figura["color"],(A,B,C))
    

def escribir_texto(screen,texto, posicion, size = 48,color = green):
    """Escribe el encabezado en el menu de inicio. 

    Args:
        screen (_type_): Superficie en la que se escribirá
        texto (str): El texto a escribir
        posicion (tuple): Posición donde se ubicará el centro del rectángulo que contiene al texto.
        size (int, optional): Tamaño de la fuente. Defaults to 48.
        color (tuple, optional): Color de la fuente. Defaults to green.
    Return (Rect): Devuelve el rectángulo asociado al texto
    """
    fuente = pygame.font.SysFont("comic sans ms", size)
    texto_render = fuente.render(texto, True, color)
    rect_texto = texto_render.get_rect()
    rect_texto.center = posicion
    pygame.draw.rect(screen,skyblue,rect_texto, border_radius = -1)
    screen.blit(texto_render,rect_texto)
    return rect_texto
    
    
def escribir_texto_figura(screen,perimetro,area,color,size = 36):
    """Escribe los resultados de los cálculos realizados para cada figura, en este caso perímetro y área.

    Args:
        screen (_type_): Superficie donde se escribirá el texto
        perimetro (float)): Perímetro de la figura calculado.
        area (float): Area de la figura calculada.
        color (tuple): Color de la fuente
        size (int, optional): Tamaño de la fuente. Defaults to 36.
    """
    fuente = pygame.font.SysFont("arial", size)
    texto_perimetro = "Perímetro: " + str(perimetro) + " px"
    texto_render = fuente.render(texto_perimetro, True, color)
    rect_texto = texto_render.get_rect()
    rect_texto.bottomleft = (20,520)
    pygame.draw.rect(screen,skyblue,rect_texto, border_radius = -1)
    screen.blit(texto_render,rect_texto)
    texto_area = "Area: " + str(area) +" px"
    texto_render = fuente.render(texto_area, True, color)
    rect_texto = texto_render.get_rect()
    rect_texto.bottomleft = (20,580)
    pygame.draw.rect(screen,skyblue,rect_texto, border_radius = -1)
    screen.blit(texto_render,rect_texto)
  
    
def dibujar_menu(screen,screen_w_mid,screen_h_mid):
    """Dibuja el menú de inicio. Recibe por parámetro la superficie sobre la que se dibujará, así como su ancho y alto. Devuelve los rectángulos asociados al nombre de las figuras geométricas.

    Args:
        screen (_type_): Superficie dónde se dibujará el menú
        screen_w_mid (_type_): Ancho de la superficie
        screen_h_mid (_type_): Alto de la superficie

    Returns:
        _type_: Una lista de diccionarios los cuáles contienen los datos asociados al rectángulo asociado al nombre de cada figura
    """
    escribir_texto(screen,"FIGURAS GEOMETRICAS",(screen_w_mid,50),60)
    escribir_texto(screen,"Haz click en una figura",(screen_w_mid,550),28)
    rect_1 = escribir_texto(screen,"Triángulo",((screen_w_mid-140),(screen_h_mid-100)),color = (0, 0, 255))
    rect_2 = escribir_texto(screen,"Cuadrado",((screen_w_mid+140),(screen_h_mid+100)),color = (215,41,224))
    rect_3 = escribir_texto(screen,"Rectángulo",((screen_w_mid-140),(screen_h_mid+100)),color = (255,255,0))
    rect_4 = escribir_texto(screen,"Círculo",((screen_w_mid+140),(screen_h_mid-100)),color = (255, 0, 0))
    lista_cuadrados = [{"rect":rect_1,"tipo":"triángulo"},{"rect":rect_2,"tipo":"cuadrado"},{"rect":rect_3,"tipo":"rectángulo"},{"rect":rect_4,"tipo":"círculo"}]
    return lista_cuadrados    
    

def gestionar_calculo_y_grafica(screen,figura,imagen,rect):
    """Dependiendo de la figura a mostrar, la dibuja llamando a la función correspondiente; realiza los calculos requeridos llamando a las funciones y luego los escribe en pantalla.

    Args:
        screen (_type_): Superficie dónde se dibujará la figura solicitada
        figura (_type_): Diccionario con los datos asociados a la figura a mostrar
        imagen (_type_): Imagen utilizada para cerrar la ventana a dibujar.
        rect (_type_): El rectángulo asociado a la imagen de cierre.
    """
    perimetro = 0
    area = 0
    if figura["tipo"] == "círculo":
        dibujar_circulo(screen,figura)
        perimetro = calcular_perimetro_circulo(figura)
        area = calcular_area_circulo(figura)
    elif figura["tipo"] == "rectángulo":
        dibujar_rectangulo(screen,figura)
        perimetro = calcular_perimetro_rectangulo(figura)
        area = calcular_area_rectangulo(figura)
    elif figura["tipo"] == "triángulo":
        dibujar_triangulo(screen,figura)
        perimetro = calcular_perimetro_triangulo(figura)
        area = calcular_area_triangulo(figura)
    elif figura["tipo"] == "cuadrado":
        dibujar_cuadrado(screen,figura)
        perimetro = calcular_perimetro_cuadrado(figura)
        area = calcular_area_cuadrado(figura)
    escribir_texto_figura(screen,perimetro,area,figura["color"])
    screen.blit(imagen,rect.topleft)
 
    

    


    
 
    
    
    
        
    
    
    
    
    
    
    
    
    
    

    
    
    
