#Doble Enlazados


class Node:
    def __init__(self, value):
        # Stores the node value
        self.value = value
        
        # Pointer to the next node
        self.next = None
        
        # Pointer to the previous node
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
        
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        
        new_node.prev = self.tail
        self.tail.next = new_node
        
        
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        
        new_node.next = self.head
        self.head.prev = new_node
        
        # Update head
        self.head = new_node

    def delete(self, data):
        
        if self.head is None:
            return

        
        if self.head.value == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return

        current = self.head

        
        while current is not None and current.value != data:
            current = current.next

        
        if current is None:
            return

        
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return

        
        current.prev.next = current.next
        current.next.prev = current.prev

    def print_forward(self):
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

    def print_backward(self):
        current = self.tail

        if current is None:
            print("List is empty.")
            return

        while current is not None:
            print(current.value, end="")
            if current.prev is not None:
                print(" -> ", end="")
            current = current.prev

        print()


dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()     
dll.print_backward()    

dll.prepend("X")

dll.print_forward()     
dll.print_backward()    

dll.delete("B")

dll.print_forward()     
dll.print_backward()    