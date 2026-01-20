class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class singlylinkedlist:
    def __init__(self,head=None):
        self.head=head

    def insertatend(self,value):
        temp = Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next = temp
        
        else:
            self.head =temp

    def printLL(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data,end='->')
            t1=t1.next
        print(t1.data)

obj = singlylinkedlist()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.printLL()

