import sohoc

print("=== CHƯƠNG TRÌNH SỐ HỌC ===")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
n = int(input("Nhập số nguyên n: "))

print(f"→ Ước chung lớn nhất của {a} và {b}: {sohoc.Ucln(a, b)}")
print(f"→ Bội chung nhỏ nhất của {a} và {b}: {sohoc.Bcnn(a, b)}")
print(f"→ Tổng các ước của {n}: {sohoc.SumDivisor(n)}")

