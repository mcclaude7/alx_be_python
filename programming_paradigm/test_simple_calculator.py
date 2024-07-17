import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)

    def test_substraction(self):
        self.assertEqual(self.calc.substract(3,2),1)
        self.assertEqual(self.calc.substract(5,6),-1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,2),4)
        self.assertEqual(self.calc.multiply(3,2),6)

    def test_division(self):
        self.assertEqual(self.calc.divide(9,3),3)
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(5,0),None)

if __name__ == "__main__":
    unittest.main()