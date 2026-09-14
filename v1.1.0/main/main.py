from . import operaciones as oper
from . import interfaz_cli as inter

def bulcle_ejecución_principal():
    while True:
        inter.ver_titulo()
        inter.ver_menu()
        intervenir_flujo, opcion_introducida = procesar_opcion()
        if intervenir_flujo is True:
            continue
        elif intervenir_flujo is False:
            break
        else:
            print('''
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~    INICIANDO MÓDULO DE OPERACIONES ...    ~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        procesar_operacion(opcion_introducida)
        inter.limpiar_consola()
          

def procesar_opcion():
    try:
        opcion_solicitada = inter.solicitud_opcion()
    except ValueError as error:
        inter.ver_error(error)
        inter.limpiar_consola()
        return True, None
    if opcion_solicitada == 0:
        inter.ver_salida()
        inter.limpiar_consola()
        return False, opcion_solicitada
    return None, opcion_solicitada
def procesar_operacion(opcion_introducida):
    try:
        num1, num2 = inter.solicitud_operandos(opcion_introducida)
        match opcion_introducida:
            case 1:
                resultado = oper.adicion(num1, num2)
            case 2:
                resultado = oper.sustraccion(num1, num2)
            case 3:
                resultado = oper.multiplicacion(num1, num2)
            case 4:
                resultado = oper.division(num1, num2)
            case 5:
                resultado = oper.potenciacion(num1, num2)
            case 6:
                resultado = oper.radicacion(num1, num2)
            case _:
                return opcion_introducida
        inter.ver_resultado(opcion_introducida, resultado)
    except ValueError as error:
        inter.ver_error(error)
        return False



if __name__ == "__main__":

    bulcle_ejecución_principal()