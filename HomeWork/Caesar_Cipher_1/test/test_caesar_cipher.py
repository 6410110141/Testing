from program.caesar_cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):

    def test_give_middle_Outz_shift_2_should_okffng_Qwvb(self):
        data = "middle-Outz"
        shift = 2
        expect_output = "okffng-Qwvb"
        result = caesarCipher(data, shift)
        self.assertEqual(result, expect_output)
    def test_give_mi48dd5le_O248utz_shift_2_should_okffng_Qwvb(self):
        data = "mi48dd5le-O248utz"
        shift = 2
        expect_output = "ok48ff5ng-Q248wvb"
        result = caesarCipher(data, shift)
        self.assertEqual(result, expect_output)
    def test_give_6410110141_shift_5_should_okffng_Qwvb(self):
        data = "6410110141"
        shift = 5
        expect_output = "6410110141"
        result = caesarCipher(data, shift)
        self.assertEqual(result, expect_output)
    def test_give_xdfhgdfghdfdle_Outdhdfhsdfbz_shift_10_should_okffng_Qwvb(self):
        data = "xdfhgdfghdfdle-Outdhdfhsdfbz"
        shift = 10
        expect_output = "hnprqnpqrnpnvo-Yednrnprcnplj"
        result = caesarCipher(data, shift)
        self.assertEqual(result, expect_output)