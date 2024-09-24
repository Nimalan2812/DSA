class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            newnode.prev = self.temp
            self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp.next is not None:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print(self.temp.data)
        print("\nIn Reverse : ")
        while self.temp is not None:
            print(self.temp.data, end=" ")
            self.temp = self.temp.prev

    def insert_at_front(self, data):
        newnode = Node(data)
        self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self, data):
        newnode = Node(data)
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        newnode.prev = self.temp
        self.temp.next = newnode

    def insert_at_middle(self, data, pos):
        newnode = Node(data)
        i = 1
        self.temp = self.head
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        newnode.next = self.temp.next
        newnode.prev = self.temp
        self.temp.next.prev = newnode
        self.temp.next = newnode

    def delete_at_front(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        self.temp = self.head
        while self.temp.next.next is not None:
            self.temp = self.temp.next
        self.temp.next = None

    def delete_at_middle(self, pos):
        self.temp = self.head
        i = 1
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next
        self.temp.next.prev = self.temp

obj = DLL()

while True:
    print("""\n1.create
2.display
3.insert_at_front
4.insert_at_end
5.insert_at_middle
6.delete_at_front
7.delete_at_end
8.delete_at_middle
9.exit""")
    ch = int(input("Enter choice : "))
    if ch == 1:
        data = int(input("Enter data : "))
        obj.create(data)
    elif ch == 2:
        obj.display()
    elif ch == 3:
        data = int(input("Enter data : "))
        obj.insert_at_front(data)
    elif ch == 4:
        data = int(input("Enter data : "))
        obj.insert_at_end(data)
    elif ch == 5:
        data = int(input("Enter data : "))
        pos = int(input("Enter Position : "))
        obj.insert_at_middle(data,pos)
    elif ch == 6:
        obj.delete_at_front()
    elif ch == 7:
        obj.delete_at_end()
    elif ch == 8:
        pos = int(input("enter Position : "))
        obj.delete_at_middle(pos)
    elif ch == 9:
        break
    else:
        print("Invalid Choice")
