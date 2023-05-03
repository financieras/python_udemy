# Módulo figuras.py
# creamos clases como Figura, Rectangulo, Circulo
# y la función probar_figura
import math

class Figura():
    def __init__(self, nombre):
        self.nombre = nombre
    def area(self):
        pass
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self, base, altura):
        Figura.perimetro(self)
        return 2*(base+altura)

class Circulo(Figura):
    def __init__(self, nombre, radio):
        Figura.__init__(self, nombre)
        self.radio = radio

    def area(self, radio):
        Figura.area(self)
        return math.pi()*radio**2

    def perimetro(self, radio):
        Figura.perimetro(self)
        return 2*math.pi*radio
    