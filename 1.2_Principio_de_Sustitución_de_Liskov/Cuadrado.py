from Figura import Figura

class Cuadrado(Figura):

  def __init__(self, lado):
    self.lado = lado

  def area(self):
    return f"Soy el area del cuadrado:  {self.lado*self.lado}"

  def perimetro(self):
    return f"Soy el perimetro del cuadrado: {self.lado*4}"
