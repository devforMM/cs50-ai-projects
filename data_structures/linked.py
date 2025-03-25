class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
class Linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        
    def insert(self,value):
        new_node=Node(value)
        self.tail.next=new_node
        self.tail=new_node
        
    def pop_end(self):
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        self.tail=temp
        
    def pop_debut(self):
        temp=self.head.next
        self.head.next=None
        self.head=temp
    def get_element(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
                
    def print_list(self):
        while self.head!=None:
            print(self.head.value)
            self.head=self.head.next
    def length(self):
        length=0
        while self.head!=None:
            self.head=self.head.next
            length+=1
        return length
    def insert_at_index(self,index,value):
        new_node=Node(value)
        if index==0:
            temp=self.head
            self.head=new_node
            self.head.next=temp
        else:
            prev=self.get_element(index-1)
            prev.next=new_node
            new_node.next=self.get_element(index)
            
        
    def pop_element(self,index):
        prev=self.get_element(index-1)
        e=self.get_element(index)
        prev.next=e.next
        e.next=None
        
        
        
        
            
        

                
        
        
        
    
linked_list=Linked_list(4)
linked_list.insert(5)
linked_list.insert(6)
linked_list.insert(7)
linked_list.insert(8)
linked_list.insert(9)
linked_list.pop_element(2)
linked_list.print_list()

