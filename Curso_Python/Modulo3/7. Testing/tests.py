import unittest

def double(a): return a*2
def sum(a,b): return a+b  
def is_even(a): return 1 if a%2 == 0 else 0

class PruebasFunciones(unittest.TestCase):

    def test_double(self):
        self.assertEqual(double(4),8)

    def test_sum(self):
        #TODO
        self.assertEqual(sum(2,4), 6)

    def test_is_even(self):
        #TODO
        self.assertEqual(is_even(4),1)

if __name__ == '__main__':
    unittest.main()