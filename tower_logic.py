from node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.is_empty():
            poppedvalue = self.top.value
            self.top = self.top.next
            return poppedvalue
        return None
             
    def is_empty(self):
        return self.top is None
    
    def create_new_stack(self):
        self.top = None
    
    def peek(self):
        return self.top.value 
    
    def display(self):
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return result
            
        