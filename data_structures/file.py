class  Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class File:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
    def emfiler(self,value):
        new_node=Node(value)
        self.tail.next=new_node
        self.tail=new_node
    def defiler(self):
        self.head=self.head.next
        
        
    def print_file(self):
        while self.head!=None:
            print(self.head.value)
            self.head=self.head.next
    def is_empt(self):
        if self.head==None:
            return True
        return False

ma_file=File(20)
ma_file.emfiler(30)
ma_file.emfiler(40)
ma_file.defiler()
ma_file.print_file()

        