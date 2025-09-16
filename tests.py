#chatgpt told me to use unittest with the assert equals and assert raises
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 6), 4)

    def test_multiply(self):
        with self.assertRaises(ValueError):
            calculator.multiply(4, "a")

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_square_root(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

if __name__ == "__main__":
    unittest.main()