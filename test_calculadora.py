# Import del módulo unittest para poder realizar pruebas unitarias
import unittest 

# Import de la clase Calculadora desde el archivo calculadora.py
from calculadora import Calculadora

# Definición de la clase de pruebas que hereda de unittest.TestCase
class TestCalculadora(unittest.TestCase):
    def setUp(self): 
        self.calc = Calculadora()

    # Prueba del método suma
    def test_suma(self):
        self.assertEqual(self.calc.suma(3, 2), 5)
        # Prueba de la suma de dos ceros
        self.assertEqual(self.calc.suma(0, 0), 0)
        #prueba de metodo de resta
        def test_resta(self):
            self.assertEqual(self.calc.resta(5, 2), 3)
            # prueba de la resta de dos ceros
            self.assertEqual(self.calc.resta(0, 5), -5)
#prueva de metodo de multiplicacion

        def test_mutipliacion(self):
            self.assertEqual(self.calc.multiplicacion(2, 3), 6)
            # prueba de la multiplicacion de dos ceros
            self.assertEqual(self.calc.multiplicacion(0, 0), 0)
            # prueba de la division por cero
        def test_division(self):
         self.assertEqual(self.calc.division(10, 2), 5)
        # prueba de la division de dos ceros
        self.assertEqual(self.calc.division(0, 5), 0)
        # prueba de la division por cero
        self.assertEqual(self.calc.division(5, 0), "No se puede dividir por cero")
        # prueba la división exacta
        self.assertEqual(self.calc.division(9, 3), 3)
        # rueba la división con resultado decimal
        self.assertEqual(self.calc.division(7, 2), 3.5)
        # prueba con división periódica usando assertAlmostEqual para comparar con precisión limitada
        self.assertAlmostEqual(self.calc.division(10, 4), 3.3333, places=4)

# Bloque de condición que permite ejecutar las pruebas directamente
if __name__ == "__main__":  
    # Inicializar la ejecución de todas las pruebas definidas
    unittest.main()
