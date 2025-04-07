#a)
n = int(input("Nhap so tu nhien n: "))
#b)
print("Day n so nguyen to dau tien: ")
for i in range(2, n):
    so_nt = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            so_nt = False
            break
    if so_nt:
        print(i, end = " ")
            
        