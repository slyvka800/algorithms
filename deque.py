class Deque:
    class Node:
        def __init__(self, new_value):
            self.value = new_value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, new_value):
        new_node = self.Node(new_value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node
        self.head = new_node


    def push_right(self, new_value):
        new_node = self.Node(new_value)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node

    def pop_left(self):
        ex_head = self.head
        if self.head is None:
            return
        if ex_head.next is not None:
            ex_head.next.prev = None
        else:
            self.tail = None
        self.head = ex_head.next
        return ex_head.value

    def pop_right(self):
        ex_tail = self.tail
        if self.tail is None:
            return
        if ex_tail.prev is not None:
            ex_tail.prev.next = None
        else:
            self.head = None
        self.tail = ex_tail.prev
        return ex_tail.value

    def deque_to_list(self):
        output = list()
        curr = self.head
        while curr is not None:
            output.append(curr.value)
            curr = curr.next
        return output

    def find_by_id(self, id):
        i=0
        curr = self.head
        while i < id and curr is not None:
            curr = curr.next
            i += 1

        if curr is None:
            return

        return curr.value

    def find_by_value(self, value):
        i=0
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return i
            curr = curr.next
            i += 1

        return None