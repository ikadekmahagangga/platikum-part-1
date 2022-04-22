deret = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 15, 10, 11, 12, 13,14]
print(deret)
deret.append('1')
deret.append('2')
deret.append('3')
deret.append('4')

print("hasil", deret)


#linklist
class maku:
    class node:
        def __init__(self, data):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def push(self, element):
        if self.head == None:
            self.head = self.node(element)
            self.tail = self.head
        else:
            self.tail.next = self.node(element)
            self.tail = self.tail.next
