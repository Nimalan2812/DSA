class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top==None:
            print("overflow")
        else:
            self.top=self.top.next
    def peek(self):
        print(self.top.data)
obj=stack()
while 1:
    print(" 1.push 2.pop 3.peek")
    ch=int(input("enter coice:"))
    if ch==1:
         data=int(input("enter data:"))
         obj.push(data)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.peek()
    else:
        print("choose coorect option")
