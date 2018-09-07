import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
import testdata

class testcls1(unittest.TestCase):
    def setUp(self):
        print('{0} {1} {2}'.format('*' * 10, __class__.__name__, '*' * 10))

    @testdata.TestData
    def test1(self, dataobj):
        print('test: data is: {}'.format(dataobj))
        print('test: this test1 in {}'.format(__class__.__name__))

    def test2(self):
        print('test: this is a test case without testdata decorator')
        print('test: this test2 in {}'.format(__class__.__name__))


class testcls2(unittest.TestCase):
    def setUp(self):
        print('{0} {1} {2}'.format('*' * 10, __class__.__name__, '*' * 10))

    @testdata.TestData
    def test1(self, dataobj):
        print('test: data is: {}'.format(dataobj))
        print('test: this test1 in {}'.format(__class__.__name__))

    def test2(self):
        print('test: this is a test case without testdata decorator')
        print('test: this test2 in {}'.format(__class__.__name__))


if __name__ == '__main__':
    unittest.main()
