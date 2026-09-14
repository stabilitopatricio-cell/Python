import unittest
from unittest.mock import patch
from main import main

class TestIntegrationMain(unittest.TestCase):
    @patch("builtins.input", return_value=3)
    def test_procesar_opcion(self, input_simulado):
        intervenir_flujo, opcion = main.procesar_opcion()

        self.assertFalse(intervenir_flujo)
        self.assertEqual(opcion, 3)

    @patch("builtins.input", side_effect=["5", "3"])
    @patch("builtins.print")
    def test_procesar_operacion(self, print_simulado, input_simulado):
        main.procesar_operacion(1)

        print_simulado("El resultado es : 8.0")