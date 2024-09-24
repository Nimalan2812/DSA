class Stack:
    def create(self):
        self.list=[]
    def is_Empty(self):
        return len(self.list)==0
    def push(self,item):
        self.list.append(item)
        print(f"Pushed {item} in the stack")
    def pop(self):
        if self.is_Empty():
            print("Underflow")
        else:
            self.list.pop()
            print(f"Popped {item} from the stack")
    def peek(self):
        if self.is_Empty():
            print("Stack is Empty")
        else:
            print("The Topmost element is",self.list[-1])
    def display(self):
        print("Stack Elements:",self.list)


obj=Stack()
while 1:
    print("1.Create,2.Push,3.Pop,4.Peek,5.Display,6,Exit")
    choice=int(input("Enter the Choice:"))
    if choice==1:
        obj.create()
    elif choice==2:
        item=int(input("enter the item"))
        obj.push(item)
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.display()
    elif choice==6:
        print("Thank You")
        break
