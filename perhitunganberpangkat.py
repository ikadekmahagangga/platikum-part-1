a = int(input("masukan sebuah nilai = "))

def maku(a):
    maki = (a*a)
    print("luas kuadrat adalah : ", maki)
maku(a)

if (a % 2 ==0):
    print("nilai tersebut bersifat genap")
else:
    print("nilai tersebut bersifat ganjil")