print("Nhap cac phan tu cua tap A=:")
chuoi_A = input("A = ")
A = set()

for ky_tu in chuoi_A:
    A.add(ky_tu)

print("Nhap cac phan tu cua tap B:")
chuoi_B = input("B = ")
B = set()

for ky_tu in chuoi_B:
    B.add(ky_tu)
chung = A & B  

print("Tap hop A la =:", A)
print("Tap hop B la=:", B)
print("Cac phan tu chung cua A va B la=:", chung)