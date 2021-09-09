import unittest
from merge_sort import merge_sort, SortOrder

arr = [2,4,4,6,43,2,4,65,6]


class MergeSortTest(unittest.TestCase):

    def test_inputArraySortingCheck(self):
        merge_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_AscArrayAscSortCheck(self):
        asc_arr = [i for i in range(100)]
        merge_sort(asc_arr)
        self.assertEqual(asc_arr, sorted(asc_arr))

    def test_AscArrayDescSortCheck(self):
        asc_arr = [i for i in range(100)]
        merge_sort(asc_arr, SortOrder.DESC)
        self.assertEqual(asc_arr, sorted(asc_arr, reverse=True))

    def test_DescArrayDescSortCheck(self):
        desc_arr = [i for i in range(100, 0, -1)]
        merge_sort(desc_arr, SortOrder.DESC)
        self.assertEqual(desc_arr, sorted(desc_arr, reverse=True))

    def test_DescArrayAscSortCheck(self):
        desc_arr = [i for i in range(100, 0, -1)]
        merge_sort(desc_arr, SortOrder.ASC)
        self.assertEqual(desc_arr, sorted(desc_arr))
