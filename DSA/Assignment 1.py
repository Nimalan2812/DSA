#TEAM 7
# Name:D.NIMALAN
#Reg.No: 23110033

#Write a python program create a Class for printing the following pattern
# * * * *
# * * * *
# * * * *
# * * * *
# * * * *
#2.Write a python program to count number of objects created
#1
class pattern:
    def __init__(self,rows,column):
        self.rows=rows
        self.column=column
    def display(self):
        for i in range(self.rows):
            print("*" *self.column)
a=pattern(5,4)
a.display()

print("----------------------------------------------")
#2
class ObjectCount:
    object_count = 0
    def __init__(self):
        ObjectCount.object_count += 1
a1 = ObjectCount()
a2 = ObjectCount()
a3 = ObjectCount()
print("Number of objects created:", ObjectCount.object_count)


