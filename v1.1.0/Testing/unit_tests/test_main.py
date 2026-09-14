import unittest
from unittest.mock import patch
from main import main

class TestMain (unittest.TestCase):

    @patch("main.main.inter.solicitud_opcion")
    def test_procesar_opcion_valida (self, solicitud_opcion):
        solicitud_opcion.return_value = 3
        intervenir_flujo, opcion = main.procesar_opcion()
        self.assertIsNone(intervenir_flujo)
        self.assertEqual(opcion, 3)

    @patch("main.main.inter.ver_salida")
    @patch("main.main.inter.limpiar_consola")
    @patch("main.main.inter.solicitud_opcion")
    def test_procesar_opcion_salida (self, solicitud_opcion, ver_salida, limpiar_consola):
        solicitud_opcion.return_value = 0
        intervenir_flujo, opcion = main.procesar_opcion()
        self.assertFalse(intervenir_flujo)
        self.assertEqual(opcion, 0)
        ver_salida.assert_called_once()
        limpiar_consola.assert_called_once()

    @patch("main.main.inter.ver_error")
    @patch("main.main.inter.limpiar_consola")
    @patch("main.main.inter.solicitud_opcion")
    def test_procesar_opcion_ValueError (self, solicitud_opcion, ver_error, limpiar_consola):
        solicitud_opcion.side_effect = ValueError("Opción inválida")
        intervenir_flujo, opcion = main.procesar_opcion()
        self.assertTrue(intervenir_flujo)
        self.assertIsNone(opcion)
        ver_error.assert_called_once()
        limpiar_consola.assert_called_once()


    @patch("main.main.inter.solicitud_operandos")
    @patch("main.main.inter.ver_resultado")
    def test_procesar_operacion(self, ver_resultado, solicitud_operandos):
        solicitud_operandos.return_value = (1.0, 2.0)
        casos = [
            (1, "adicion", 3.0),
            (2, "sustraccion", -1.0),
            (3, "multiplicacion", 2.0),
            (4, "division", 0.5),
            (5, "potenciacion", 0.1),
            (6, "radicacion", 0.7071067811865476),
        ]
        for opcion, nombre_operacion, espectativa in casos:
            with patch(f"main.main.oper.{nombre_operacion}", return_value=espectativa) as operacion:
                main.procesar_operacion(opcion)
                operacion.assert_called_once_with(1.0, 2.0)
                ver_resultado.assert_called_with(opcion, espectativa)
            ver_resultado.reset_mock()

    @patch("main.main.inter.ver_error")
    @patch("main.main.inter.solicitud_operandos")
    def test_procesar_operacion_ValueError(self, solicitud_operandos, ver_error):
        solicitud_operandos.side_effect = ValueError("Operando inválido")
        resultado = main.procesar_operacion(1)
        ver_error.assert_called_once()
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()

    print("\n=======PRUEBA DE ALCANCE==========\n")