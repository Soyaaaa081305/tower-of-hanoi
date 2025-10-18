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
    
    def peek(self):
        return self.top.value 
<<<<<<< HEAD:stack.py
        
=======
>>>>>>> 296c79e11a73a73cc466f5698c91e1ac3921ea35:tower_logic.py
