class Stack:
    def __init__(self):
        self.top=-1
    def create(self,size):
        self.size=size
        self.stack=[None]*size

    def is_full(self):
        return self.top==self.size-1
    def is_empty(self):
        return self.top==-1
    def push(self,item):
        if self.is_full():
            print("overflow")
        else:
            self.top+=1
            self.stack[self.top]=item
            print(f"pushed {item} to Stack")
    def pop(self):
        if self.is_empty():
            print("underflow")
        item=self.stack[self.top]
        self.stack[self.top]=None
        self.top-=1
        print(f"Popped {item} from Stack")
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(self.stack[self.top])

    def display(self):
        print(self.stack)

obj=Stack()
while 1:
    print("1.Create,2.push,3.pop,4.peek,5.display,6.exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        size=int(input("Enter the size"))
        obj.create(size)
    elif choice==2:
        item=int(input("Enter the item"))
        obj.push(item)
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.display()
    
        
