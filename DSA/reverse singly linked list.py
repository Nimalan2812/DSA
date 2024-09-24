class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

obj = LinkedList()
while True:
    print("1.Insert, 2.Reverse, 3.Display")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the Data: "))
        obj.insert(data)
    elif choice == 2:
        obj.reverse()
    elif choice == 3:
        obj.printList()
    else:
         print("invalid choice")
     
