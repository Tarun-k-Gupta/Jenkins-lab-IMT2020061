#!/usr/bin/python3
import unittest

from function import fact

class TestFact(unittest.TestCase):
        
    def testFact1(self):
        data = 5
        result = fact(data)
        self.assertEqual(result, 100)
        
    def testFact2(self):
        data = -3
        result = fact(data)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()