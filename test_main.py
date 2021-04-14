from unittest import TestCase
from main import complete_array


class Test(TestCase):

    def test_complete_array_case_1(self):
        self.assertEqual([1, 2, 3, 4, 5], complete_array([2, 1, 4, 5]))

    def test_complete_array_case_2(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], complete_array([4, 2, 9]))

    def test_complete_array_case_3(self):
        # validates result is [1..60]
        self.assertEqual([x for x in range(1, 61)], complete_array([58, 60, 55]))
