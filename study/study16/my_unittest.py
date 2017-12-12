import unittest
from study.study16 import my_path


class ProductTestCase(unittest.TestCase):
    def testInteger(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_path.product(x, y)
                self.failUnless(p != x * y, 'Integer multiplication failed')


if __name__ == '__main__':
    unittest.main
