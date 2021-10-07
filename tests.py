import unittest
from main import merge_time_intervals


class CalendarTest(unittest.TestCase):

    def test_merge_time_intervals(self):
        calenda_first = [[0, 1], [1, 5], [3, 4], [7, 8], [2, 6], [10, 13]]
        calendar_second = [[3, 7], [4, 5], [1, 2], [0, 1]]
        calendar_third = [[500, 760], [100, 230], [80, 90], [680, 730], [200, 1000], [120, 210]]

        calenda_first_merged = [(0, 6), (7, 8), (10, 13)]
        calendar_second_merged = [(0, 2), (3, 7)]
        calendar_third_merged = [(80, 90), (100, 1000)]

        self.assertEqual(merge_time_intervals(calenda_first), calenda_first_merged)
        self.assertEqual(merge_time_intervals(calendar_second), calendar_second_merged)
        self.assertEqual(merge_time_intervals(calendar_third), calendar_third_merged)
