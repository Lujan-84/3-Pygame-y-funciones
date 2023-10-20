

def detectar_colision(rect_1,rect_2):
    for r1,r2 in [(rect_1,rect_2),(rect_2,rect_1)]:
        return punto_en_rectangulo(r1.bottomleft,r2) or punto_en_rectangulo(r1.bottomright,r2) or punto_en_rectangulo(r1.topleft,r2) or punto_en_rectangulo(r1.topright,r2)
    
def punto_en_rectangulo(punto,rect)->bool:
    x,y = punto
    return rect.bottom >= y and rect.top <= y and rect.left <= x and rect.right >= x



    