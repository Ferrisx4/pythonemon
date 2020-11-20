# -*- coding: latin-1 -*-
import unittest
from ..combat import calculate_effectiveness

class TestCombat(unittest.TestCase):
    #def test_calculate_damage(self):
    #    self.assertEqual(calculate_damage(50, 50, 40, 30, 'Rock'), 2, "Should be 2")

    def test_calculate_effectiveness(self):
        self.assertEqual(calculate_effectiveness('Electric','Water','Flying'),2.0,"Should be 2")