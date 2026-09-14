import subprocess



def ver_titulo():
    titulo = '''
====== Calculadora básica ======
      ( v 0.1 by Stapaher ) 
    (                       )'''
    print(titulo)
def ver_menu():
    menu = '''        Menú de opciones

1. Adición         2. Sustracción
3. Multiplicación  4. División
5. Potenciación    6. Radicación
           
           0. Salir
================================
'''
    print(menu)
def solicitud_opcion():
    try:
        opcion_solicitada = int(input("Introduce una opción : "))
    except ValueError:
        raise ValueError('''
        ##############################################
            ERROR DE FORMATO EN SOLICITUD DE OPCIÓN 
        ----------------------------------------------
        M..., Yo que tú, me replantearía esa decisión.
        ############################################## \n
        ''')

    if opcion_solicitada in range(0, 7):
        return opcion_solicitada
    else: 
        raise ValueError('''
        ##############################################
            ERROR DE RANGO EN SOLICITUD DE OPCIÓN
        ----------------------------------------------
        M..., Yo que tú, me replantearía las opciones.
        ##############################################\n
        ''')
def solicitud_operandos(opcion_solicitada):
    match opcion_solicitada:
        case 1:
            num1 = "primer sumando"
            num2 = "segundo sumando"
        case 2:
            num1 = "minuendo"
            num2 = "sustraendo"
        case 3:
            num1 = "primer factor"
            num2 = "segundo factor"
        case 4:
            num1 = "dividendo"
            num2 = "divisor"
        case 5:
            num1 = "número base"
            num2 = "exponente"
        case 6:
            num1 = "radicando"
            num2 = "índice"
        case _:
            raise ValueError("")
    try:
        operando1_solicitado = float(input(f"\nIntroduce el {num1}: " ))
        operando2_solicitado = float(input(f"\nIntrocuce el {num2}: " ))
    except:
        raise ValueError('''
        ##############################################
           ERROR DE FORMATO EN SOLICITUD DE OPERANDO 
        ----------------------------------------------
        M..., Yo que tú, me replantearía la ejecución.
        ############################################## \n
        ''')
    return operando1_solicitado, operando2_solicitado
def ver_resultado(opcion_solicitada, resultado):
    match opcion_solicitada:
        case 1:
            opcion = "El resultado"
        case 2:
            opcion = "La diferencia"
        case 3:
            opcion = "El producto"
        case 4:
            opcion = "El cociente"
        case 5:
            opcion = "La potencia"
        case 6:
            opcion = "La raíz"
        case _:
            raise ValueError("\n Error inesperado. <<< Lo siento >>> \n")# Aquí no se debería producir ningún error.
    try:
        print(f"\n{opcion} es : {resultado}\n")
    except:
        raise ValueError("\n Error inesperado. <<< Lo siento >>> \n ")# Aquí no se debería producir ningún error.
def ver_error(error):
    print(error)
def ver_salida():
    salida = '''
=========================================================
(:>   >>> Espero haberte ayudado, ¡Hasta luego! <<<   <:)
=========================================================

'''
    print(salida)
def limpiar_consola():
    input("Presiona > Enter < para continuar...")
    subprocess.run("cls", shell=True)


