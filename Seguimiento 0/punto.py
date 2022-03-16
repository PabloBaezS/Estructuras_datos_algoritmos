import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanciaAlOrigen(self):
        return math.sqrt(self.x**2 + self.y**2)

    def anguloConElEjeX(self):
        return math.atan2(self.y, self.x)

    def distanciaAOtroPunto(self, punto2):
        deltax = self.x - punto2.x
        deltay = self.y - punto2.y
        return math.sqrt( deltax**2 + deltay**2)

# INPUT
x1, y1 =  map(int, input().split())
x2, y2 =  map(int, input().split())

punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

print(round( punto1.distanciaAlOrigen(), 2 ))
print(round(  punto1.anguloConElEjeX(), 2))
print(round(  punto1.distanciaAOtroPunto(punto2), 2))