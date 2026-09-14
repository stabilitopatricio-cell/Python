# README — Versión 1.1.0

## 1. Identificación de la versión

**Versión:** 1.1.0
**Tipo:** Evolución estructural y consolidación del Testing

## 2. Objetivo de la versión

Esta versión tiene como objetivo consolidar el sistema de pruebas automatizadas del proyecto y establecer una estructura de Testing diferenciada por niveles de comprobación.

La aplicación mantiene su funcionamiento como calculadora mediante interfaz de consola. 

La principal evolución de esta versión se encuentra en la verificación automatizada del comportamiento de la aplicación.

## 3. Cambios realizados

### 3.1. Reorganización del Testing

Las pruebas se han separado en tres niveles:

```text
Testing/
    unit_tests/
    integration_tests/
    e2e_tests/
```

Esta organización permite diferenciar entre la comprobación de funciones individuales, la comunicación entre módulos y el funcionamiento de la aplicación mediante un flujo completo.

### 3.2. Testing unitario

Se han establecido pruebas unitarias para los módulos principales:

* `operaciones.py`
* `interfaz_cli.py`
* `main.py`

Estas pruebas verifican individualmente los comportamientos relevantes de cada módulo.

### 3.3. Testing de integración

Se han incorporado pruebas específicas para comprobar la comunicación entre los módulos de la aplicación.

Se utilizan casos representativos para verificar que el flujo de procesamiento de opciones y operaciones funciona correctamente sin repetir las comprobaciones realizadas mediante las pruebas unitarias.

### 3.4. Testing E2E

Se ha incorporado una prueba de extremo a extremo que reproduce un flujo completo de utilización de la calculadora:

```text
Inicio -> operación -> resultado -> menú -> salida
```

La prueba permite verificar que los diferentes componentes funcionan conjuntamente durante una ejecución completa.

## 4. Documentación

La documentación del Testing se ha reorganizado en cuatro documentos:

```text
Testing/
    Testing_es.md
    UnitaryTesting_es.md
    IntegrationTesting_es.md
    e2eTesting_es.md
```

Cada documento tiene una responsabilidad específica y se ha reducido la duplicación de información entre ellos.

El documento general describe la arquitectura y los criterios comunes, mientras que los documentos específicos desarrollan cada nivel de pruebas.

## 5. Validación

La batería completa de pruebas ha sido ejecutada mediante `unittest`.

Resultado:

```text
Ran 17 tests

OK
```

Distribución actual:

* 14 pruebas unitarias.
* 2 pruebas de integración.
* 1 prueba E2E.

Todas las pruebas definidas superan correctamente las comprobaciones establecidas.

## 6. Estado de la versión

La versión 1.1.0 establece un punto de control funcional y estructural del proyecto.

La aplicación de consola dispone ahora de una batería de pruebas automatizadas organizada por niveles y de una documentación específica para cada nivel.

Este estado constituye la base para la siguiente evolución del proyecto: la incorporación de una **interfaz gráfica de usuario (GUI)**.
