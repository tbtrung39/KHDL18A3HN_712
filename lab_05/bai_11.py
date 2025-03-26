#Cách 1:
n = input("Nhap chuoi nhi phan: ")
ket_qua = int(n, 2)
print("Chuoi thap phan tuong ung la: ", ket_qua)

#Cách 2:
n = input("Nhap chuoi nhi phan: ")
ket_qua = 0
for i in range(len(n)):
    ket_qua = ket_qua*2 + int(n[i])
print("So thap phan tuong ung la: ", ket_qua)