#LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        
        if self.head is None:
            self.head = new_node
            return

        
        current = self.head
        while current.next is not None:
            current = current.next

        
        current.next = new_node

    def delete(self, data):
        # If list is empty
        if self.head is None:
            return

        
        if self.head.value == data:
            self.head = self.head.next
            return

        
        current = self.head
        while current.next is not None and current.next.value != data:
            current = current.next

        
        if current.next is not None:
            current.next = current.next.next

    def print_all(self):
        current = self.head

        if current is None:
            print("List is empty.")
            return

        while current is not None:
            print(current.value, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next

        print()  



ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.insert_back(30)

ll.print_all()   

ll.delete(10)

ll.print_all()   