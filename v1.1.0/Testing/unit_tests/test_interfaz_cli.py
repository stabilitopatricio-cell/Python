import unittest
from main import interfaz_cli
from unittest.mock import patch


class TestInterfaz_Cli(unittest.TestCase):
    def test_solicitud_opcion(self):
        with patch("builtins.input", return_value="abc"):
            with self.assertRaises(ValueError): interfaz_cli.solicitud_opcion()
        with patch("builtins.input", return_value="3"):
            self.assertEqual(interfaz_cli.solicitud_opcion(), 3)
        with patch("builtins.input", return_value="8"):
            with self.assertRaises(ValueError): interfaz_cli.solicitud_opcion()

    def test_solicitud_operandos(self):
        with patch("builtins.input", side_effect=("5", "3")):
            self.assertEqual(interfaz_cli.solicitud_operandos(1), (5.0, 3.0))
        with patch("builtins.input", side_effect=("5.2", "3.5")):
                    self.assertEqual(interfaz_cli.solicitud_operandos(1), (5.2, 3.5))
        with patch("builtins.input", side_effect=("a", "3")):
            with self.assertRaises(ValueError): interfaz_cli.solicitud_operandos(1)
        with patch("builtins.input", side_effect=("5", "3")):
            with self.assertRaises(ValueError): interfaz_cli.solicitud_operandos(7)

    def test_ver_resultado(self):
        with patch("builtins.print") as mock_print:
              interfaz_cli.ver_resultado(1, 5.0)
        mock_print.assert_called_once_with("\nEl resultado es : 5.0\n")
        with patch("builtins.print") as mock_print:
                      interfaz_cli.ver_resultado(2, 5.0)
        mock_print.assert_called_once_with("\nLa diferencia es : 5.0\n")
        with patch("builtins.print") as mock_print:
                      interfaz_cli.ver_resultado(3, 5.0)
        mock_print.assert_called_once_with("\nEl producto es : 5.0\n")
        with patch("builtins.print") as mock_print:
                      interfaz_cli.ver_resultado(4, 5.0)
        mock_print.assert_called_once_with("\nEl cociente es : 5.0\n")
        with patch("builtins.print") as mock_print:
                      interfaz_cli.ver_resultado(5, 5.0)
        mock_print.assert_called_once_with("\nLa potencia es : 5.0\n")
        with patch("builtins.print") as mock_print:
                      interfaz_cli.ver_resultado(6, 5.0)
        mock_print.assert_called_once_with("\nLa raíz es : 5.0\n")
        with self.assertRaises(ValueError): interfaz_cli.ver_resultado(7, 5.0)







if __name__ == "__main__":
    unittest.main()