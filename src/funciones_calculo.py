from datos_figuras import *
from math import pi
# Areas
def calcular_area_rectangulo(figura:dict)->float:
    ancho,alto = figura["dimensiones"]
    return ancho*alto

def calcular_area_cuadrado(figura:dict)->float:
    return figura["dimensiones"]**2

def calcular_area_circulo(figura:dict)->float:
    return round(pi*figura["dimensiones"]**2,2)

def calcular_area_triangulo(figura:dict)->float:
    a,b,c = figura["dimensiones"]
    return a*b/2

# Perímetros
def calcular_perimetro_rectangulo(figura:dict)->float:
    ancho,alto = figura["dimensiones"]
    return 2*(ancho+alto)

def calcular_perimetro_cuadrado(figura:dict)->float:
    return figura["dimensiones"]*4

def calcular_perimetro_circulo(figura:dict)->float:
    return round(2*pi*figura["dimensiones"],2)

def calcular_perimetro_triangulo(figura):
    lado_a,lado_b,lado_c = figura["dimensiones"]
    return lado_a + lado_b + lado_c



       
    
    
    



