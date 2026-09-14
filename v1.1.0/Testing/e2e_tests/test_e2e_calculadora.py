import unittest
from unittest.mock import patch
from main import main

class TestE2eCalculadora(unittest.TestCase):
    @patch("builtins.input", side_effect=[1, 5, 3, "", 0, ""])
    def test_flujo_completo_calculadora(self, input_simulado):
        main.bulcle_ejecución_principal()