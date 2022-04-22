class hacimaru:
    def __init__(self,node,vaule):
        self.node = node
        self.vaule = vaule
        self.next = None
    def getNode(self):
        return self.getNode
    def getVaule(self):
        return self.getVaule
    def getNext(self):
        return self.getNext
    def setNode(self,node):
        self.node = node
    def setVaule(self,vaule):
        self.vaule = vaule
    def setNext(self,next):
        self.next = next

class maku:
    def __init__(self):
        self.head = None
        self.size = 0
    def __len__(self):
        return self.size
    def isempty(self):
        return self.size == 0
    def push(self,data):
        self.head = hacimaru(self.head,data)
        self.size += 1
    def pop(self):
        simpan = self.head.getVaule(self)
        self.head = self.head.getNext(self)
        self.size -= 1
        return simpan
    def top(self):
        return self.head.getVaule()

s = maku()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)

maku = int(input("masukan sebuah nilai = "))
s.push(maku)
print(len(s))