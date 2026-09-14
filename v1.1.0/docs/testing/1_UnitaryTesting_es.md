# Pruebas unitarias

## 1. Objetivo

Las pruebas unitarias verifican el comportamiento de funciones individuales de la aplicación de forma aislada.

El objetivo es comprobar que cada función cumple su responsabilidad independientemente del funcionamiento de otros componentes del sistema.

El proyecto utiliza `unittest` y, cuando es necesario aislar dependencias, `unittest.mock`.

## 2. Organización

Las pruebas unitarias se encuentran en:

```text
Testing/
    unit_tests/
        test_interfaz_cli.py
        test_main.py
        test_operaciones.py
```

Cada archivo corresponde al módulo de producción que se está verificando.

## 3. Pruebas de `operaciones.py`

`test_operaciones.py` comprueba individualmente las seis operaciones disponibles:

| Operación      | Función            |
| -------------- | ------------------ |
| Adición        | `adicion()`        |
| Sustracción    | `sustraccion()`    |
| Multiplicación | `multiplicacion()` |
| División       | `division()`       |
| Potenciación   | `potenciacion()`   |
| Radicación     | `radicacion()`     |

Los casos de prueba incluyen diferentes valores y combinaciones de operandos, incluyendo valores positivos, negativos, cero y números decimales cuando resulta relevante para la operación.

También se comprueba el comportamiento excepcional de entradas y valores no válidos.

## 4. Pruebas de `interfaz_cli.py`

`test_interfaz_cli.py` comprueba las funciones de la interfaz que contienen lógica susceptible de validación automatizada:

* `solicitud_opcion()`
* `solicitud_operandos()`
* `ver_resultado()`

Se verifican principalmente:

* Conversión de entradas.
* Validación de opciones.
* Selección de comportamiento.
* Generación de errores.
* Generación de los mensajes correspondientes a las operaciones.

Las funciones dedicadas exclusivamente a mostrar contenido estático o ejecutar acciones directas sin lógica significativa no disponen de pruebas unitarias específicas.

## 5. Pruebas de `main.py`

`test_main.py` comprueba individualmente las funciones que contienen lógica de coordinación:

* `procesar_opcion()`
* `procesar_operacion()`

Se verifican tanto los comportamientos normales como los casos en los que se produce `ValueError`.

Las dependencias de `main.py` se sustituyen durante estas pruebas para aislar las funciones sometidas a comprobación.

Por ejemplo, se sustituyen temporalmente las funciones de `interfaz_cli` y `operaciones` mediante `patch()` para controlar su comportamiento y comprobar cómo responde `main.py`.

## 6. Aislamiento mediante `unittest.mock`

Cuando una prueba unitaria depende de otra función o módulo, la dependencia se sustituye temporalmente mediante `patch()`.

El objetivo es que la prueba compruebe exclusivamente el comportamiento de la función bajo prueba.

* `patch()`: Sustituye temporalmente el objeto indicado durante la ejecución de la prueba, y debe aplicarse sobre la dependencia tal como es utilizada por el módulo bajo prueba.

* `return_value`: Define el valor que devolverá el objeto simulado cuando sea llamado.

* `side_effect`: Permite definir un comportamiento alternativo al realizar la llamada. Entre otros usos, permite provocar deliberadamente una excepción para comprobar el tratamiento de errores.

## 7. Aserciones

Las pruebas utilizan las aserciones proporcionadas por `unittest` para comparar el comportamiento obtenido con el esperado.

Entre las utilizadas se encuentran:

* `assertEqual()` para comparar valores.
* `assertAlmostEqual()` para resultados de coma flotante.
* `assertTrue()` y `assertFalse()` para estados booleanos.
* `assertIsNone()` para comprobar valores `None`.
* `assertRaises()` para comprobar excepciones.

Las pruebas que utilizan objetos simulados también pueden verificar que una dependencia haya sido llamada correctamente mediante las aserciones proporcionadas por `Mock`.

## 8. Criterio de aislamiento

Una prueba unitaria no pretende demostrar que varios módulos funcionan correctamente juntos.

Cuando una función depende de otros componentes, estos se sustituyen cuando su comportamiento no forma parte del objetivo de la prueba.

De esta forma se mantiene la separación entre los objetos de comprobación.

## 9. Estado actual

Las pruebas unitarias forman parte de la batería general de 17 pruebas del proyecto.

Actualmente comprenden:

* 6 pruebas para `operaciones.py`.
* 3 pruebas para `interfaz_cli.py`.
* 5 pruebas para `main.py`.

Estas pruebas se ejecutan conjuntamente con las pruebas de integración y E2E, pero mantienen su responsabilidad específica de verificar comportamientos individuales.
