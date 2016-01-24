#!/usr/bin/env python3

import unittest
import church_nums as cn

class ChurchNumeralsTest(unittest.TestCase):

    def test_church_to_int(self):
        five = lambda f: lambda x: f(f(f(f(f(x)))))
        self.assertEqual(cn.church_to_int(five), 5)

    def test_zero(self):
        self.assertEqual(cn.church_to_int(cn.zero), 0)

    def test_one(self):
        self.assertEqual(cn.church_to_int(cn.one), 1)

    def test_successor(self):
        two = cn.successor(cn.one)
        self.assertEqual(cn.church_to_int(two), 2)

        three = cn.successor(cn.successor(cn.one))
        self.assertEqual(cn.church_to_int(three), 3)

if __name__ == '__main__':
    unittest.main()
