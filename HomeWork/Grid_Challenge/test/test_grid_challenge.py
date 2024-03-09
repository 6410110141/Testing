from program.grid_challenge import gridChallenge
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_should_YES(self):
         data = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
         expect_output = "YES"
         result = gridChallenge(data)
         self.assertEqual(expect_output, result)
    def test_give_ebacd_fghij_aaaaa_trpqs_xywuv_should_NO(self):
         data = ['ebacd', 'fghij', 'aaaaa', 'trpqs', 'xywuv']
         expect_output = "NO"
         result = gridChallenge(data)
         self.assertEqual(expect_output, result)
    def test_give_xhkz_achd_wbcf_should_NO(self):
         data = ['xhkz', 'achd', 'wbcf']
         expect_output = "NO"
         result = gridChallenge(data)
         self.assertEqual(expect_output, result)
