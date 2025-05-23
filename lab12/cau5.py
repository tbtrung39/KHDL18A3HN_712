def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return int(str(n) * n) + tong_S2(n - 1)

try:
    n = int(input("Nhập n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương.")

    print("S1 =", tong_S1(n))
    print("S2 =", tong_S2(n))

except ValueError as ve:
    print("Lỗi giá trị:", ve)
except RecursionError:
    print("Lỗi đệ quy: giá trị n quá lớn.")
except Exception as e:
    print("Lỗi khác:", e)