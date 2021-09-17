from deque import Deque
import os

if __name__ == '__main__':
    deque = Deque()

    deque.push_left(1)
    deque.push_right(2)
    deque.push_left(3)
    deque.push_left(5)
    deque.push_right(8)

    # print(deque.find_by_value(8))

    print(deque.deque_to_list())

    print(deque.pop_left())
    print(deque.deque_to_list())

    print(deque.pop_right())
    print(deque.deque_to_list())

    command = "python3 -m unittest test_dequeue.py"
    os.system(command)