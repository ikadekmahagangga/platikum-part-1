#class untuk node dari singgle link list
class Node(object):

    def __init__(self, data=none, next_node=none):
        self.data = data
        self.next_node = next_node

#mengambil data dari node

    def get_data(self):
        return self.get_data

#mengambil node berikutnya

    def get_next(self):
        return self.next_node

#menentukan node berikutnya

    def set_next(self, new_next):
        self.next_node = new_next

#membuat class untuk single link list
class LinkedList(object):
    def __init__(self, head=none):
            self.head = head

#menambahkan node baru
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

#menampilkan data
    def showData(self):
        print("-------------------------")
        print("|    menampilkan isi data     |")
        print("|    Node -> Next Node     |")
        print("-------------------------")
        current_node = self.head
        while current_node is not none:
            print("current_node.data),
            print("   ->   "),
            print("current_node.next_node.data) if hasattr(current_node.next_node, 'data') else Node
            current_node = current_node.next_node

#menu utama
     #def mainmenu(self):
      #  pilih = "y"
       # while (pilih == "y"):
        #    print("-------------------------")
         #   print("|    menu aplikasi      |")
          #  print("-------------------------")
           # print("| 1. Tambah data        |")
           # pilihan = str(input("Masukan pilihan anda: "))
          #  if (pilihan ==1):
           #     obj = str(input("Masukan data yang akan ditambahkan: "))
            #    self.insert(obj)
          #  else:
           #     print("Pilihan tidak tersedia")

#if __name__ == '__main__':
 #   l = LinkedList()
  #  l.mainmenu()
        #print("| 2. Lihat data         |")
        #print("| 3. Edit data          |")
        #print("| 4. Hapus data         |")
        #print("| 5. Keluar             |")

#melihat panjang dari linked list
    def size(self):
        current_node = self.head
        found = False
        while current and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
        return found

    def size(self):
        current_node = self.head
        found = False
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    def delete(self, data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())
        return found