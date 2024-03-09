from program.cat_and_mouse import cat_and_mouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_give_1_2_3_Cat_B(self):
        x,y,z = 1,2,3 
        expect_output = 'Cat B'
        result = cat_and_mouse(x,y,z)
        self.assertEqual(expect_output, result)
    def test_give_20_50_22_Cat_B(self):
        x,y,z = 20,50,22
        expect_output = 'Cat A'
        result = cat_and_mouse(x,y,z)
        self.assertEqual(expect_output, result)
    def test_give_45_55_50_Cat_B(self):
        x,y,z = 45,55,50
        expect_output = 'Mouse C'
        result = cat_and_mouse(x,y,z)
        self.assertEqual(expect_output, result)
    def test_give_1_50_200_None(self):
        x,y,z = -1,50,200
        expect_output = None
        result = cat_and_mouse(x,y,z)
        self.assertEqual(expect_output, result)
