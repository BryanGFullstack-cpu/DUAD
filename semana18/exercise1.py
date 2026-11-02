#estructura de datos sort


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()


def bubble_sort_linked_list(ll):
    if ll.head is None:
        return

    swapped = True
    while swapped:
        swapped = False
        current = ll.head
        prev = None

        while current is not None and current.next is not None:
            nxt = current.next
            if current.value > nxt.value:
                swapped = True
                current.next = nxt.next
                nxt.next = current
                if prev is None:
                    ll.head = nxt
                else:
                    prev.next = nxt
                prev = nxt
            else:
                prev = current
                current = current.next



values = [5, 3, 1, 4, 2]
ll = LinkedList()
for v in values:
    ll.append(v)

bubble_sort_linked_list(ll)
ll.print_all()

