#Estructura de objetos


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        # If the stack is empty, nothing to remove
        if self.top is None:
            print("Stack is empty. Cannot pop.")
            return None
        

        removed_value = self.top.value
        self.top = self.top.next
        return removed_value
    
    def print_stack(self):
        current = self.top
        print("STACK:")
        while current is not None:
            print(f"  → {current.value}")
            current = current.next


#por si acaso

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()

print("Pop:", stack.pop())
print("Pop:", stack.pop())

stack.print_stack()

#los agregue en main por error
