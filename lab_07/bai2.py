# bai 2
Numbers = []
print("hay nhap cac so tu nhien va go x de ket thuc")
while True:
    dlieu = input("Hay nhap so: ")
    if dlieu.lower() == 'x':
        break
    if dlieu.isdigit():  # kiem tra so da nhap co phai la so tu nhien hay khoong
        so = int(dlieu)
        Numbers.append(so)
    else:
        print("Vui long chi nhap so tu nhien!!!!!!!!!")
A = set(Numbers)
print("\nDanh sách Numbers là:", Numbers)
print("\nTập hợp A la ",A)
