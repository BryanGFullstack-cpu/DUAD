#Estructuras de datos



class Node:
    def __init__(self, value):
        self.value = value
        
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        
        self.tail.next = new_node
        
        
        self.tail = new_node

    def dequeue(self):
        
        if self.head is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        
        removed_value = self.head.value
        
        
        self.head = self.head.next
        
        
        if self.head is None:
            self.tail = None
        
        return removed_value

    def print_all(self):
        current = self.head
        
        if current is None:
            print("Queue is empty.")
            return
        
        
        while current is not None:
            print(current.value, end="")
            
            if current.next is not None:
                print(" -> ", end="")
            
            current = current.next
        
        print()  



q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()   

print(q.dequeue()) 

q.print_all()   