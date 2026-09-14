# Prueba E2E (Extremo a Extremo)

## 1. Objetivo

Las pruebas E2E (End-to-End) verifican el comportamiento de la aplicación mediante un flujo completo de utilización.

A diferencia de las pruebas unitarias y de integración, no se comprueban funciones o comunicaciones concretas de forma aislada. 

Se ejecuta el flujo completo de la aplicación y se comprueba que puede desarrollarse desde la entrada del usuario hasta su finalización.

## 2. Organización

La prueba E2E se encuentra en:

```text
Testing/
    e2e_tests/
        test_e2e_calculadora.py
```

## 3. Flujo comprobado

Actualmente se utiliza un único escenario representativo:

```text
Inicio
|_  Seleccionar adición
    |_  Introducir primer operando
        |_  Introducir segundo operando
            |_  Mostrar resultado
                |_  Volver al menú
                    |_  Seleccionar salida
                        |_  Finalizar aplicación
```

La prueba utiliza la ejecución real de:

```Python
main.bulcle_ejecución_principal()
```

y reproduce las entradas del usuario mediante una secuencia controlada de llamadas a `input()`.

La secuencia utilizada representa:

```text id="l8k3md"
1 → seleccionar adición
5 → primer operando
3 → segundo operando
"" → continuar después del resultado
0 → salir
"" → continuar después del mensaje de salida
```

## 4. Criterio de la prueba

La prueba no sustituye las funciones internas de la aplicación.

El objetivo es comprobar que los componentes que ya han sido verificados individualmente y mediante integración pueden ejecutarse conjuntamente siguiendo un flujo completo.

La simulación se limita a la interacción externa con `input()`, necesaria para reproducir las acciones del usuario sin intervención manual.

## 5. Estado actual

Actualmente existe un escenario E2E automatizado que completa correctamente el flujo definido.

Esta prueba forma parte de la batería general de 17 pruebas automatizadas del proyecto.
