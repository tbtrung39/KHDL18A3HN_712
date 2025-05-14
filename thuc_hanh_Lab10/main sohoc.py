import sohoc
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("Ước chung lớn nhất:", sohoc.tim_ucln(a, b))
print("Bội chung nhỏ nhất:", sohoc.tim_bcnn(a, b))
n = int(input("Nhập số nguyên n để tính tổng các ước: "))
print("Tổng các ước của", n, "là:", sohoc.SumDivisor(n))
