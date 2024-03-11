from Calculadora import Calculadora


def main():
    calculadora = Calculadora()
    
    num1 = 10
    num2 = 20
    
    resultado_suma = calculadora.sumar(num1, num2)
    resultado_resta = calculadora.restar(num1, num2)
    resultado_multiplicacion = calculadora.multiplicar(num1, num2)
    resultado_division = calculadora.dividir(num1, num2)
    print(f"La suma de {num1} y {num2} es {resultado_suma}")
    print(f"La resta de {num1} y {num2} es {resultado_resta}")
    print(f"La multiplicacion de {num1} y {num2} es {resultado_multiplicacion}")
    print(f"La division de {num1} y {num2} es {resultado_division}")


if __name__ == "__main__":
  main()
