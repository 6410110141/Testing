from program.funny_string import funnyString
import unittest

class TestFunnyString(unittest.TestCase):
    def test_give_acxz_should_Funny(self):
         data = 'acxz'
         expect_output = "Funny"
         result = funnyString(data)
         self.assertEqual(expect_output, result)
    def test_give_acxz_should_Not_Funny(self):
         data = 'bcxz'
         expect_output = "Not Funny"
         result = funnyString(data)
         self.assertEqual(expect_output, result)
    def test_give_bcxzdkfhgsdfg_should_Not_Funny(self):
         data = 'bcxzdkfhgsdfg'
         expect_output = "Not Funny"
         result = funnyString(data)
         self.assertEqual(expect_output, result)