class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Pile:
    
    def __init__(self,value):
        new_node=Node(value)
        self.tail=new_node
        self.head=new_node
    def emplier(self,value):
        new_node=Node(value)
        self.tail.next=new_node
        self.tail=new_node
    def depiler(self):
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        self.tail=temp
        self.tail.next=None
    def print_pile(self):
        temp=self.head
        print(temp)
        while temp!=self.tail:
            temp=temp.next
            print(temp.value)
            
            

ma_pile=Pile(10)
ma_pile.emplier(11)
ma_pile.emplier(12)
ma_pile.emplier(13)

ma_pile.print_pile()