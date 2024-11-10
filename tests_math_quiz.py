import unittest
from math_quiz import _rndm_number,_random_operator, _math_problem

class TestMathQuizFunctions(unittest.TestCase):

    def test_rndm_number(self):
        """Test if _rndm_number generates a number within the specified range."""
        min_value = 1
        max_value = 10
        random_number = _rndm_number(min_value, max_value)
        self.assertGreaterEqual(random_number, min_value)
        self.assertLessEqual(random_number, max_value)

    def test_random_operator(self):
        """Test if _random_operator returns a valid operator (+, -, *)."""
        operator = _random_operator()
        self.assertIn(operator, ['+', '-', '*'])

    def test_math_problem(self):
        """Test if _math_problem returns a correct problem string and answer."""
        num1, num2 = 5, 3
        # Test addition
        problem, answer = _math_problem(num1, num2, '+')
        self.assertEqual(problem, "5 + 3")
        self.assertEqual(answer, 8)

        # Test subtraction
        problem, answer = _math_problem(num1, num2, '-')
        self.assertEqual(problem, "5 - 3")
        self.assertEqual(answer, 2)

        # Test multiplication
        problem, answer = _math_problem(num1, num2, '*')
        self.assertEqual(problem, "5 * 3")
        self.assertEqual(answer, 15)

if __name__ == "__main__":
    unittest.main()

