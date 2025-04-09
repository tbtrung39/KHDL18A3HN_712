Numbers = []
print("Nhap cac so tu nhien(nhap e de ket thuc): ")
while True:
    so = input("Nhap so: ")
    if so.lower() == "e":
        break
    if so.isdigit():
        Numbers.append(int(so))
    else:
        print("Vui long nhap so tu nhien!!!")
A = set(Numbers)
print("Danh sach Numbers: ", Numbers)
print("Tap hop A: ", A)