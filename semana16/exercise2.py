#Double ended Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_right(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("Deque is empty. Cannot pop_left.")
            return None

        removed_value = self.head.value

        if self.head == self.tail:
           self.head = None
           self.tail = None
        removed_value

        self.head = self.head.next
        self.head.prev = None
        return removed_value

    def pop_right(self):
        if self.tail is None:
            print("Deque is empty. Cannot pop_right.")
            return None

        removed_value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_value

        self.tail = self.tail.prev
        self.tail.next = None
        return removed_value

    def print_deque(self):
        current = self.head
        print("DEQUE:")
        while current is not None:
            print(f"  ↔ {current.value}")
            current = current.next



dq = Deque()

dq.push_left(10)
dq.push_right(20)
dq.push_left(5)
dq.push_right(30)

dq.print_deque()

print("pop_left:", dq.pop_left())
print("pop_right:", dq.pop_right())

dq.print_deque()


#me diverti con este ejercicio, me gusta la idea de una estructura de datos que permita insertar y eliminar elementos desde ambos extremos. Es como tener lo mejor de ambos mundos entre una pila y una cola. Además, la implementación con nodos enlazados me pareció bastante elegante