import unittest
import operaciones  

class TestOperaciones(unittest.TestCase):
    def test_adicion(self):
        self.assertEqual(operaciones.adicion(1, 1), 2)
        self.assertEqual(operaciones.adicion(1, -1), 0)
        self.assertEqual(operaciones.adicion(-10, -100), -110)
        self.assertEqual(operaciones.adicion(-1.8, 1), -0.8)
        self.assertEqual(operaciones.adicion(1.2, 1.5), 2.7)
        self.assertEqual(operaciones.adicion(0, 0), 0)
        self.assertEqual(operaciones.adicion(0, 1), 1)
        self.assertEqual(operaciones.adicion(1, 0), 1)
        self.assertEqual(operaciones.adicion(1000, 10000), 11000)

    def test_sustraccion(self):
        self.assertEqual(operaciones.sustraccion(5, 5), 0)
        self.assertEqual(operaciones.sustraccion(10, -10), 20)
        self.assertEqual(operaciones.sustraccion(-5, 5), -10)
        self.assertEqual(operaciones.sustraccion(-5, -5), 0)
        self.assertAlmostEqual(operaciones.sustraccion(-5.1, 3.1), -8.2)
        self.assertAlmostEqual(operaciones.sustraccion(5.8, 3.1), 2.7)
        self.assertEqual(operaciones.sustraccion(0, 5), -5)
        self.assertEqual(operaciones.sustraccion(5, 0), 5)
        self.assertEqual(operaciones.sustraccion(0, 0), 0)
        self.assertEqual(operaciones.sustraccion(5_000_000, 2_000_000_000), -1995000000)

    def test_multiplicacion(self):
        self.assertEqual(operaciones.multiplicacion(5, 5), 25)
        self.assertEqual(operaciones.multiplicacion(5, -5), -25)
        self.assertEqual(operaciones.multiplicacion(-5, -5), 25)
        self.assertAlmostEqual(operaciones.multiplicacion(5.25, 1.25), 6.5625)
        self.assertAlmostEqual(operaciones.multiplicacion(-5.3, 5), -26.5)
        self.assertEqual(operaciones.multiplicacion(5, 0), 0)
        self.assertEqual(operaciones.multiplicacion(0, 5), 0)
        self.assertEqual(operaciones.multiplicacion(0, 0), 0)
                
    def test_division(self):
        self.assertEqual(operaciones.division(10, 2), 5)
        self.assertEqual(operaciones.division(-10, 2), -5) 
        self.assertEqual(operaciones.division(10, -2), -5)
        self.assertEqual(operaciones.division(-10, -2), 5)
        self.assertAlmostEqual(operaciones.division(5.8, 2), 2.9)
        self.assertAlmostEqual(operaciones.division(-5.8, 2), -2.9)
        self.assertEqual(operaciones.division(0, 5), 0)
        self.assertEqual(operaciones.division(5, 1), 5)
        
        with self.assertRaises(ValueError): operaciones.division(5, 0)

    def test_potenciacion(self):
        self.assertEqual(operaciones.potenciacion(2, 3), 8)
        self.assertEqual(operaciones.potenciacion(-2, 3), -8)
        self.assertAlmostEqual(operaciones.potenciacion(2, -3), 0.125)
        self.assertAlmostEqual(operaciones.potenciacion(-2, -3), -0.125)
        self.assertAlmostEqual(operaciones.potenciacion(2.5, 2), 6.25)
        self.assertEqual(operaciones.potenciacion(5, 0), 1)
        self.assertEqual(operaciones.potenciacion(0, 5), 0)
        self.assertEqual(operaciones.potenciacion(10, 1), 10)

    def test_radicacion(self):
            self.assertAlmostEqual(operaciones.radicacion(9, 2), 3)
            self.assertAlmostEqual(operaciones.radicacion(16, 2), 4)
            self.assertAlmostEqual(operaciones.radicacion(25, 2), 5)
            self.assertAlmostEqual(operaciones.radicacion(8, 3), 2)
            self.assertAlmostEqual(operaciones.radicacion(27, 3), 3)
            self.assertAlmostEqual(operaciones.radicacion(32, 5), 2)
            self.assertAlmostEqual(operaciones.radicacion(2.25, 2), 1.5)
            self.assertAlmostEqual(operaciones.radicacion(0, 2), 0)

if __name__ == "__main__":
    unittest.main()