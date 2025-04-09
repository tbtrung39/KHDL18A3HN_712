#a)
n = int(input("Nhap so tu nhien n la: "))
#b)
print("Day n so nguyen to dau tien la: ")
for i in range(2, n):
    so_nguyen_to = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(i, end = " ")
             