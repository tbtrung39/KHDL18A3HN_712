def tinh_S1(n):
    return sum(range(1, n + 1))

def tinh_S2(n):
    return sum(i ** 2 for i in range(1, n + 1))

try:
    n = int(input("Nhập n: "))
    if n <= 0:
        print("n phải lớn hơn 0")
    else:
        print("S1 =", tinh_S1(n))
        print("S2 =", tinh_S2(n))
except ValueError:
    print("Lỗi: n phải là số nguyên")