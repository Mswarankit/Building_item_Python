# Building a class stack

class Stack:
    def __init__(self):
        self.items = []   # First we are trying to take an empty stack

    def is_empty(self):
        return self.items == [] # To check whether that is empty

    def push(self, item):
        self.items.append(item) # Trying to add items in stack using append it will append in last place

    def pop(self):
        return self.items.pop() # pop the first element from the stack

    def peek(self):
        return self.items[len(self.items) - 1] # To check top most element call peek

    def size(self):
        return len(self.items) # tell the size of the stack


