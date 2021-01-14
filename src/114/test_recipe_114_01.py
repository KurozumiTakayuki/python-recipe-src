# 以下のコマンドで実行します
# python -m unittest test_recipe_114_01.py 

import unittest

class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('全体前処理')

    @classmethod
    def tearDownClass(cls):
        print('全体後処理')

    def setUp(self):
        print('テスト前処理')

    def tearDown(self):
        print('テスト後処理')

    def test_sample1(self):
        print("単体テスト1実行")

    def test_sample2(self):
        print("単体テスト2実行")
