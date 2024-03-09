from program.alternating_characters import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_give_AAAA_should_3(self):
        data = 'AAAA'
        expect_output = 3
        result = alternatingCharacters(data)
        self.assertEqual(expect_output, result)
    def test_give_BBBBB_should_4(self):
        data = 'BBBBB'
        expect_output = 4
        result = alternatingCharacters(data)
        self.assertEqual(expect_output, result)
    def test_give_ABABABAB_should_0(self):
        data = 'ABABABAB'
        expect_output = 0
        result = alternatingCharacters(data)
        self.assertEqual(expect_output, result)
    def test_give_BABABA_should_0(self):
        data = 'BABABA'
        expect_output = 0
        result = alternatingCharacters(data)
        self.assertEqual(expect_output, result)

    def test_give_AAABBB_should_4(self):
        data = 'AAABBB'
        expect_output = 4
        result = alternatingCharacters(data)
        self.assertEqual(expect_output, result)
