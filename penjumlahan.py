a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

def tambah (a,b):
    hasil = (a+b)
    print ("hasil dari tambah",hasil)
hasil = tambah(a,b)

def kurang (a,b):
    hasil = (a-b)
    print (hasil)
hasil = kurang(a,b)

def kali (a,b):
    hasil = (a*b)
    print (hasil)
hasil = kali(a,b)

def bagi (a,b):
    hasil = (a/b)
    print (hasil)
hasil = bagi(a,b)

def modulus (a,b):
    hasil = (a%b)
    print (hasil)
hasil = modulus(a,b)

def pangkat (a,b):
    hasil = (a**b)
    print (hasil)
hasil = pangkat(a,b)

def pembulatan (a,b):
    hasil = (a//b)
    print (hasil)
hasil = pembulatan(a,b)
