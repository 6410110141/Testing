from program.two_characters import alternate
import unittest

class TestAlternate(unittest.TestCase):
    def test_give_beabeefeab_should_5(self):
        data = 'beabeefeab'
        expect_output = 5
        result = alternate(data)
        self.assertEqual(expect_output, result)
    def test_give_abcd_should_2(self):
        data = 'abcd'
        expect_output = 2
        result = alternate(data)
        self.assertEqual(expect_output, result)
    def test_give_xxxxyyy_should_0(self):
        data = 'xxxxyyy'
        expect_output = 0
        result = alternate(data)
        self.assertEqual(expect_output, result)
    def test_give_aaaaaaaa_should_0(self):
        data = 'aaaaaaaa'
        expect_output = 0
        result = alternate(data)
        self.assertEqual(expect_output, result)
    def test_give_abcdefghifklmnopqrstuvwxyz_should_2(self):
        data = 'abcdefghijklmnopqrstuvwxyz'
        expect_output = 2
        result = alternate(data)
        self.assertEqual(expect_output, result)