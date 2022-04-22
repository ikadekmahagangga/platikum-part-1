from collections import deque

Antrian = deque([1,2,3,4,5])
print("Data Sekarang : ", Antrian)

# Menambahkan Data
Antrian.append(6)
print("Data Masuk    : ", 6)
print("Data Sekarang : ", Antrian)

Antrian.append(7)
print("Data Masuk    : ", 7)
print("Data Sekarang : ", Antrian)

# Mengurangi Antrian
Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Antrian.append(8)
print("Data Masuk    : ", 8)
print("Data Sekarang : ", Antrian)


