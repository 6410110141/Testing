from program.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_5_7_11_is_prime(self):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_6_7_8_is_not_prime(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    def test_give_n1_n2_n3_is_not_prime(self):
        prime_list = [-1, -2, -3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    def test_give_0_is_not_prime(self):
        prime_list = [0]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)