class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

ll= linkedlist()
ll.add_list(30)
print("cetak linked list")
ll.display()
ll.add_list(20)
ll.add_list(10)
ll.display()