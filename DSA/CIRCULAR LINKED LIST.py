# CIRCULAR LINKED LIST IMPLEMENTATION & DELETION

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.temp=None
        self.tail=None

    def create(self,data):
        newnode =node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
            self.tail.next = self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self

    def display(self):
        self.temp=self.head
        while self.temp.next!=self.head:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print(self.temp.data)
        print()

    def delete_at_front(self):
        self.head = self.head.next
        self.tail.next = self.head

    def delete_at_end(self):
        self.temp = self.head
        while self.temp.next.next != self.head:
            self.temp = self.temp.next
        self.temp.next.next = None
        self.temp.next = self.head
        self.tail = self.temp

    def delete_at_mid(self, pos):
        self.temp = self.head
        i = 1
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next

obj3=CLL()
while(1):
    print("""\n1.create 
2.display  
3.delete at front 
4.delete at end 
5.delete at mid 
6.exit""")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj3.create(data)
    elif choice==2:
        obj3.display()
    elif choice==3:
        obj3.delete_at_front()
    elif choice==4:
        obj3.delete_at_end()
    elif choice==5:
        pos = int(input("Enter position "))
        obj3.delete_at_mid(pos)
    elif choice==6:
        break
    else:
        print("Invalid Choice")
