#Bai10
m = input("Nhập số m: ")
n = input("Nhập số n: ")
set_m = set(m)
set_n = set(n)
chu_so_chung = set()
for i in set_m:
    if i in set_n:
        chu_so_chung.add(i)
tong = 0
for i in chu_so_chung:
    tong += int(i)
print("Các chữ số chung của", m, "và", n, "là:", chu_so_chung)
print("Tổng của các chữ số chung là:", tong)