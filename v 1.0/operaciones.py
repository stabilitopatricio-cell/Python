
def adicion(num1, num2):
    resultado = num1 + num2
    return resultado
def sustraccion(num1, num2):
    resultado = num1 - num2
    return resultado
def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado
def division(num1, num2):
    if num2 == 0:
        raise ValueError ("M..., Yo que tú me replantearía la situación.")
    resultado = num1 / num2
    return resultado
def potenciacion(num1, num2):
    resultado = num1 ** num2
    return resultado
def radicacion(num1, num2):
    resultado = num1 ** (1 / num2)
    return resultado

