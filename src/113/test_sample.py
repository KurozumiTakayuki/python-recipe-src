# test_sample.py テストをする側のコード
import unittest
import sample


class TestNumberFuncs(unittest.TestCase):

    def test_add_num(self):
        """
        add_numの単体テスト
        """
        self.assertEqual(7, sample.add_num(3, 4))

    def test_is_positive(self):
        """
        is_numの単体テスト
        """
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))
