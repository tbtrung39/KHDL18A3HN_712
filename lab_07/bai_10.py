n = input("Nhap n: ")
m = input("Nhap m: ")
n = set(n)
m = set(m)
tong = 0
for i in n:
    for j in m:
        if i == j:
            tong += int(i)
print("Tong cac chu so chung cua m va n: ", tong)
            
