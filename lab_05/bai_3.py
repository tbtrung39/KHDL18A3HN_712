n = int(input("Nhap so tu nhien n: "))
kq = " "
if n == 0:
    kq = "0"
else:
    while n>0:
        kq = str(n%2) + kq
        n = n//2
print("Chuoi nhi phan: ", kq)