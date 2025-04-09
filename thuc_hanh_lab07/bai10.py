m=input("Nhập số m: ")
n=input("Nhập số n: ")
print("Tổng các chữ số chung:",sum(int(c)for c in set(m)&set(n)))