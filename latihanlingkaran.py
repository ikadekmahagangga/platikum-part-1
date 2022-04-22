a = int(input("masukan sebuah nilai = "))
b = int(input("masukan sebuah nilai = "))
def luaslingkaran(a,b):
    luas = (a*b*b)
    print("luas lingkaran adalah= ", luas)
luaslingkaran(a,b)
#pengujian yang salah adalah kita mengisi nilai a dan b dengan tipe data string
#karena nilai a dan b adalah tipe data string maka kita harus mengubah nilai a dan b menjadi tipe data integer