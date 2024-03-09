from program.staircase import staircase
import unittest

class TestStaircase(unittest.TestCase):
    def test_give_0_will_return_None(self):
        level = 0
        pattern = '#'
        result = staircase(level, pattern)
        expected_output = None 
        self.assertEqual(result, expected_output)
    def test_give_31_will_return_None(self):
        level = 31
        pattern = '#'
        result = staircase(level, pattern)
        expected_output = None 
        self.assertEqual(result, expected_output)
    def test_give_1_will_return_None(self):
        level = 1
        pattern = '#'
        result = staircase(level, pattern)
        expected_output = "#\n"
        self.assertEqual(result, expected_output)
    def test_give_10_will_return_staircase(self):
        level = 10
        pattern = '#'
        result = staircase(level, pattern)
        expected_output = \
'         #\n' + \
'        ##\n' + \
'       ###\n' + \
'      ####\n' + \
'     #####\n' + \
'    ######\n' + \
'   #######\n' + \
'  ########\n' + \
' #########\n' + \
'##########\n'
        self.assertEqual(result, expected_output)