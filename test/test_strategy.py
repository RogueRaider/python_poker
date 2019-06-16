import unittest
from strategy import simple

class TestStringMethods(unittest.TestCase):

    def test_simple_strategy(self):
        my_strategy = simple('cards')
        self.assertEqual(my_strategy.action(), 'check')

if __name__ == '__main__':
    unittest.main()