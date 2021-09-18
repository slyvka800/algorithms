import unittest
from deque import Deque as My_deque
from collections import deque

class DequeueTest(unittest.TestCase):

    def test_push_left(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_left(1)
        my_deque.push_left(5)
        my_deque.push_left(7)
        my_deque.push_left(-4)

        my_deque_list = my_deque.deque_to_list()

        # built-in deque
        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)

        correct_deque_list = list(correct_deque)

        self.assertEqual(my_deque_list, correct_deque_list)

    def test_push_right(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_right(1)
        my_deque.push_right(5)
        my_deque.push_right(7)
        my_deque.push_right(-4)

        my_deque_list = my_deque.deque_to_list()

        # built-in deque
        correct_deque = deque()
        correct_deque.append(1)
        correct_deque.append(5)
        correct_deque.append(7)
        correct_deque.append(-4)

        correct_deque_list = list(correct_deque)

        self.assertEqual(my_deque_list, correct_deque_list)

    def test_pop_left(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_left(1)
        my_deque.push_left(5)
        my_deque.push_left(7)
        my_deque.push_left(-4)
        my_deque.pop_left()
        my_deque.pop_left()

        my_deque_list = my_deque.deque_to_list()

        # built-in deque
        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_deque.popleft()
        correct_deque.popleft()

        correct_deque_list = list(correct_deque)

        self.assertEqual(my_deque_list, correct_deque_list)

    def test_pop_right(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_left(1)
        my_deque.push_left(5)
        my_deque.push_left(7)
        my_deque.push_left(-4)
        my_deque.pop_right()
        my_deque.pop_right()

        my_deque_list = my_deque.deque_to_list()

        # built-in deque
        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_deque.pop()
        correct_deque.pop()

        correct_deque_list = list(correct_deque)

        self.assertEqual(my_deque_list, correct_deque_list)

    def test_find_by_value(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_left(1)
        my_deque.push_left(5)
        my_deque.push_left(7)
        my_deque.push_left(-4)
        my_index = my_deque.find_by_value(5)

        # built-in deque
        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_index = correct_deque.index(5, 0, 3)

        self.assertEqual(my_index, correct_index)

    def test_find_by_id(self):
        # my deque
        my_deque = My_deque()
        my_deque.push_left(1)
        my_deque.push_left(5)
        my_deque.push_left(7)
        my_deque.push_left(-4)
        my_value = my_deque.find_by_id(2)

        # built-in deque
        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_value = correct_deque[2]

        self.assertEqual(my_value, correct_value)