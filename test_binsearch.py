import unittest
from binsearch import binary_search

class MyTest(unittest.TestCase):
    
    def test_BS_simple_working(self):
        myInput = list(range(20))
        self.assertEqual(binary_search(myInput,10), 10)
    def test_BS_simple_notWorking(self):
        myInput = list(range(20))
        self.assertEqual(binary_search(myInput,21), -1)

    def test_BS_emptyList(self):
        self.assertEqual(binary_search([],10), -1)

    def test_BS_float(self):
        self.assertEqual(binary_search([1.1, 1.2, 3., 4], 1.2),1)

    def test_BS_univariateList_working(self):
        self.assertEqual(binary_search([5], 5), 0)
    def test_BS_univariateList_notWorking(self):
        self.assertEqual(binary_search([5], 4), -1)

    def test_BS_unordered(self):
        self.assertEqual(binary_search([-2, -3, 0, -4, 1],-4), -1)
    def test_BS_unordered(self):
        self.assertEqual(binary_search([1, float("inf"), 2, 4], 2), -1)

    # def test_BS_unordered(self):
    #     self.assertEqual(binary_search([-2,-3,0,1,2],0), -1)

    def test_BS_infinity_1(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0), 1)
    def test_BS_infinity_2(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], float("inf")), 3)

    def test_BS_left_1(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 2), -1)
    def test_BS_left_2(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 1), 1)

    def test_BS_right_1(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], -float("inf"), right=1), 0)
    def test_BS_right_2(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], float("inf"), right=2), -1)

    def test_BS_left_right_1(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 1, 2), 1)
    def test_BS_left_right_2(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 2, 3), -1)
    def test_BS_left_right_3(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 1, 1), 1)
    def test_BS_left_right_4(self):
        self.assertEqual(binary_search([-float("inf"), 0, 1, float("inf")], 0, 2, 2), -1)

    def test_BS_nonNumeric_1(self):
        self.assertEqual(binary_search(list('abcd'), 'c'), 2)
    def test_BS_nonNumeric_2(self):
        self.assertEqual(binary_search(list('abcd'), 'c', 2, 2), 2)
    def test_BS_nonNumeric_3(self):
        self.assertEqual(binary_search(list('abcd'), 'c', 1, 3), 2)

    def test_BS_repetition_1(self):
        self.assertTrue(binary_search([1, 1, 1], 1) in [0,1,2])
    def test_BS_repetition_2(self):
        self.assertEqual(binary_search([1, 1, 3], 2), -1)

if __name__ == '__main__':
    unittest.main()


