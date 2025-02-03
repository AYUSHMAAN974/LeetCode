class Node:
    def _init_(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head=None
        
    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def display(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="->")
                temp=temp.next
            print("None")
ll=LinkedList()
while True:
    data = input("Enter a number (or type 'exit' to stop): ")
    if data.lower() == 'exit':
        break
    ll.insert(int(data))
    
print("Linked List:")
ll.display()
