m = input("Nhập số m: ")
n = input("Nhập số n: ")

set_m = set(m)
set_n = set(n)

chung = set_m & set_n
tong = sum(int(c) for c in chung)

print("Các chữ số chung:", chung)
print("Tổng các chữ số chung:", tong)
