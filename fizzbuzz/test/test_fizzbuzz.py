from program.fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_fizz(self):
        data = 3
        expect_output = 'Fizz'
        result = fizzbuzz(data)
        self.assertEqual(expect_output, result)
    def test_give_5_should_buzz(self):
        data = 5
        expect_output = 'Buzz'
        result = fizzbuzz(data)
        self.assertEqual(expect_output, result)
    def test_give_15_should_fizzbuzz(self):
        data = 15
        expect_output = 'FizzBuzz'
        result = fizzbuzz(data)
        self.assertEqual(expect_output, result)
    def test_give_2_should_not_fizzbuzz(self):
        data = 2
        expect_output = 'not a FizzBuzz'
        result = fizzbuzz(data)
        self.assertEqual(expect_output, result)