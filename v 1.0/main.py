import operaciones as oper
import interfaz_cli as inter

def bulcle_ejecución_principal():
     while True:
          inter.ver_titulo()
          inter.ver_menu()
          opcion_solicitada = inter.solicitud_opcion()
          procesar_opcion(opcion_solicitada)

          if opcion_solicitada == 0:
               inter.ver_salida()
               break
          elif opcion_solicitada < 0 and opcion_solicitada > 6:
               continue
          else:
               print("\n ... Ingresando al módulo de operaciones ... ")
          num1, num2 = inter.solicitud_operandos(opcion_solicitada)
          procesar_operacion(opcion_solicitada, num1, num2)
          inter.limpiar_consola()
          

def procesar_opcion(opcion_solicitada):
     opcion_solicitada = inter.solicitud_opcion
     if opcion_solicitada == TypeError:
          inter.ver_error(error=TypeError)
     elif opcion_solicitada == ValueError:
          inter.ver_error(error=ValueError)
     else:
          return opcion_solicitada
def procesar_operacion(opcion_solicitada, num1, num2):
     match opcion_solicitada:
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
               return opcion_solicitada

     inter.ver_resultado(opcion_solicitada, resultado)




bulcle_ejecución_principal()