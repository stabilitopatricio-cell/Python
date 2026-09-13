# Pruebas de operaciones

## 1. Descripción

El archivo `test_operaciones.py` contiene las pruebas unitarias automatizadas correspondientes al módulo `operaciones.py`.

Las pruebas utilizan el módulo estándar `unittest` de Python y comprueban directamente el comportamiento de las funciones matemáticas, sin intervenir en la interfaz de usuario ni en el flujo principal de la aplicación.

---

## 2. Objetivo

El objetivo de estas pruebas es verificar que las operaciones matemáticas producen los resultados esperados ante diferentes tipos de entrada.

También se comprueban determinados comportamientos específicos, como la generación de una excepción al intentar realizar una división entre cero.

---

## 3. Alcance

Actualmente se prueban las seis operaciones disponibles en `operaciones.py`:

| Operación      | Función            | Prueba                  |
| -------------- | ------------------ | ----------------------- |
| Adición        | `adicion()`        | `test_adicion()`        |
| Sustracción    | `sustraccion()`    | `test_sustraccion()`    |
| Multiplicación | `multiplicacion()` | `test_multiplicacion()` |
| División       | `division()`       | `test_division()`       |
| Potenciación   | `potenciacion()`   | `test_potenciacion()`   |
| Radicación     | `radicacion()`     | `test_radicacion()`     |

Los casos utilizados incluyen, según las características de cada operación:

* Valores positivos.
* Valores negativos.
* Cero.
* Números decimales.
* Diferentes combinaciones de operandos.
* Comportamientos que deben producir una excepción.

Las pruebas se centran en la lógica matemática del módulo `operaciones.py`.

---

## 4. Organización de las pruebas

Las pruebas están organizadas según la operación matemática que se desea verificar.

Cada operación dispone de un método de prueba independiente dentro de la clase `TestOperaciones`. Dentro de cada método se agrupan los diferentes casos necesarios para comprobar el comportamiento de esa operación.

Esta organización permite:

* Identificar rápidamente qué operación presenta un fallo.
* Mantener agrupados los casos relacionados con una misma operación.
* Probar una operación sin modificar directamente las de las demás.
* Mantener una estructura sencilla y adecuada al tamaño actual del proyecto.

---

## 5. Métodos de comprobación

Las pruebas utilizan diferentes métodos de `unittest` según el tipo de resultado esperado.

### `assertEqual()`

Se utiliza cuando el resultado esperado puede compararse directamente con el resultado obtenido.

Ejemplo:

```python
self.assertEqual(operaciones.adicion(1, 1), 2)
```

### `assertAlmostEqual()`

Se utiliza para resultados numéricos en los que interviene la representación de números en coma flotante y puede existir una pequeña diferencia de precisión.

Ejemplo:

```python
self.assertAlmostEqual(operaciones.division(5.8, 2), 2.9)
```

### `assertRaises()`

Se utiliza para comprobar que una determinada operación genera la excepción esperada.

Ejemplo:

```python
with self.assertRaises(ValueError):
    operaciones.division(5, 0)
```

En este caso, la prueba verifica que `division()` no devuelve un resultado cuando el divisor es cero, sino que genera un `ValueError`.

---

## 6. Ejecución

Las pruebas pueden ejecutarse directamente desde el archivo:

```bash
python test_operaciones.py
```

También pueden ejecutarse mediante el sistema de descubrimiento de `unittest`:

```bash
python -m unittest
```

Un resultado satisfactorio indica que los casos definidos en `test_operaciones.py` han producido los resultados esperados.

Cuando una prueba falla, debe analizarse la diferencia entre el resultado obtenido y el esperado para determinar si el problema se encuentra en la implementación de la operación o en la propia prueba.

---

## 7. Estado actual

El testing del proyecto se encuentra actualmente **en desarrollo**.

Las operaciones matemáticas disponen de una primera batería de pruebas automatizadas que cubre diferentes tipos de operandos y comportamientos básicos.

Este conjunto podrá ampliarse posteriormente para incorporar nuevos casos límite, comportamientos matemáticos específicos, validaciones adicionales o nuevas funcionalidades que se incorporen al proyecto.

Este documento describe únicamente el estado actual de las pruebas de `operaciones.py`.
