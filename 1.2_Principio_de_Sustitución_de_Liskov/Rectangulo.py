from Figura import Figura


class Rectangulo(Figura):

  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho
    pass

  def area(self):
    return f"Soy el area del rectangulo {self.largo*self.ancho}"

  def perimetro(self):
    return f"Soy el perimetro del rectangulo {(self.largo*2)+(self.ancho*2)}"
