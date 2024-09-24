#Stack implementation using array
class Stack:
    def __init__(self):
        self.items = [] 
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def is_empty(self):
       return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
while 1:
    print("1. push 2.pop 3.peek 4.quit")
    ch=int(input("enterb the choice:"))
    if ch==1:
        data=int(input("enter the data:"))
        stack.push(data)
    elif ch==2:
        stack.pop()
    elif ch==3:
        stack.peek()
    elif ch==4:
        break
print("Stack size:", stack.size())
print("Top element:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Is stack empty?", stack.is_empty())
