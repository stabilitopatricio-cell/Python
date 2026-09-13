# Pruebas de `interfaz_cli.py`

## 1. Objetivo

Este documento describe las pruebas realizadas sobre las funciones de `interfaz_cli.py` que contienen lógica de validación, conversión o selección de comportamiento.

Las pruebas se realizan mediante `unittest` y `unittest.mock`, simulando las entradas y salidas de la interfaz para comprobar el comportamiento de las funciones sin depender de la interacción real con el teclado o la consola.

## 2. Funciones sometidas a prueba

Se prueban las siguientes funciones:

* `solicitud_opcion()`
* `solicitud_operandos()`
* `ver_resultado()`

Las funciones dedicadas exclusivamente a mostrar elementos estáticos de la interfaz no se incluyen en las pruebas, al no contener lógica significativa ni presentar interrelaciones que justifiquen su comprobación mediante tests automatizados.

## 3. Pruebas de `solicitud_opcion()`

La función `solicitud_opcion()` recibe una entrada mediante `input()`, la convierte a entero y comprueba que el valor se encuentre dentro del intervalo de opciones válidas.

Se comprueban tres situaciones:

### Entrada no numérica

Se simula la introducción de `"abc"`.

**Resultado esperado:** se produce `ValueError`.

### Opción válida

Se simula la introducción de `"3"`.

**Resultado esperado:** la función devuelve el entero `3`.

### Opción fuera del rango permitido

Se simula la introducción de `"8"`.

**Resultado esperado:** se produce `ValueError`.

Estas pruebas verifican tanto la conversión de la entrada como la validación del rango permitido.

## 4. Pruebas de `solicitud_operandos()`

La función `solicitud_operandos()` determina qué operandos debe solicitar según la operación seleccionada y convierte las entradas recibidas a `float`.

Se comprueban los siguientes casos:

### Operandos enteros

Se simulan las entradas `"5"` y `"3"`.

**Resultado esperado:**

```text
(5.0, 3.0)
```

### Operandos decimales

Se simulan las entradas `"5.2"` y `"3.5"`.

**Resultado esperado:**

```text
(5.2, 3.5)
```

### Operando no numérico

Se simula una entrada no convertible a `float`.

**Resultado esperado:** se produce `ValueError`.

### Opción de operación no válida

Se utiliza una opción que no corresponde con ninguna de las operaciones definidas.

**Resultado esperado:** se produce `ValueError`.

Estas pruebas permiten comprobar la selección de la operación, la conversión de los operandos y el tratamiento de entradas no válidas.

## 5. Pruebas de `ver_resultado()`

La función `ver_resultado()` selecciona el texto correspondiente a cada operación y lo muestra mediante `print()`.

Para evitar depender de la consola real, se utiliza `patch()` para simular `print()` y comprobar qué argumento recibe.

Se comprueban las seis operaciones disponibles:

1. Adición
2. Sustracción
3. Multiplicación
4. División
5. Potenciación
6. Radicación

Para cada opción se verifica que se genere el mensaje correspondiente y que incluya correctamente el resultado proporcionado.

También se comprueba una opción no válida.

**Resultado esperado:** se produce `ValueError`.

## 6. Criterio de alcance

No se han creado pruebas específicas para las funciones que únicamente muestran textos estáticos o realizan una acción directa sin lógica significativa:

* `ver_titulo()`
* `ver_menu()`
* `ver_error()`
* `ver_salida()`
* `limpiar_consola()`

La decisión se basa en mantener una relación razonable entre el valor de las pruebas y el coste de mantenerlas. Si alguna de estas funciones presentase un fallo, su comportamiento es suficientemente directo como para localizarlo directamente en su implementación.

## 7. Estado

Las pruebas descritas corresponden a la implementación actual de `test_interfaz_cli.py`.

El conjunto de pruebas de esta interfaz queda limitado deliberadamente a las funciones cuyo comportamiento puede beneficiarse de una comprobación automatizada.
