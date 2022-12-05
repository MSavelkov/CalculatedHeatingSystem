import random
import unittest
from main_window import Window

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculator = Window()

    def test_get_calculate(self):
        self.calculator.heat_load = random.randint(0, 100)
        self.calculator.temp_in = random.randint(100, 140)
        self.calculator.temp_from = random.randint(70, 90)
        self.assertTrue(self.calculator.water_consumption != 0)

if __name__ == '__main__':
    unittest.main()