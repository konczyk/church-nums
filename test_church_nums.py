#!/usr/bin/env python3

import unittest
import church_nums as cn

class ChurchNumeralsTest(unittest.TestCase):

    def test_church_to_int(self):
        five = lambda f: lambda x: f(f(f(f(f(x)))))
        self.assertEqual(cn.church_to_int(five), 5)

    def test_int_to_church(self):
        self.assertEqual(cn.int_to_church(0), cn.zero)

        three = cn.int_to_church(3)
        self.assertEqual(cn.church_to_int(three), 3)

    def test_zero(self):
        self.assertEqual(cn.church_to_int(cn.zero), 0)

    def test_one(self):
        self.assertEqual(cn.church_to_int(cn.one), 1)

    def test_successor(self):
        two = cn.successor(cn.one)
        self.assertEqual(cn.church_to_int(two), 2)

        three = cn.successor(cn.successor(cn.one))
        self.assertEqual(cn.church_to_int(three), 3)

    def test_add(self):
        zero = cn.add(cn.zero, cn.zero)
        self.assertEqual(cn.church_to_int(zero), 0)

        three = cn.add(cn.one, cn.successor(cn.one))
        self.assertEqual(cn.church_to_int(three), 3)

    def test_mul(self):
        zero = cn.mul(cn.zero, cn.one)
        self.assertEqual(cn.church_to_int(zero), 0)

        two = cn.successor(cn.one)
        three = cn.successor(two)
        six = cn.mul(two, three)
        self.assertEqual(cn.church_to_int(six), 6)

    def test_pow(self):
        one = cn.pow(cn.one, cn.zero)
        self.assertEqual(cn.church_to_int(one), 1)

        two = cn.successor(cn.one)
        three = cn.successor(two)
        eight = cn.pow(two, three)
        self.assertEqual(cn.church_to_int(eight), 8)

if __name__ == '__main__':
    unittest.main()
