from Figura import Figura
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado


def main():
    print("\n ---Principio de Sustitucion de Liskov---")
    figura = {Cuadrado(5), Rectangulo(10, 5)}
    
    for figura in figura:
      print(figura.area())
      print(figura.perimetro())


if __name__ == "__main__":
    main()
