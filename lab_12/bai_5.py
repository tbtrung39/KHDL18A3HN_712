def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return n**2 + tong_S2(n - 1)

try:
    n = input("Nhập số nguyên dương n: ")
    
    if not n.isdigit():
        raise ValueError("Lỗi: n phải là một số nguyên dương.")

    n = int(n)

    if n <= 0:
        raise ValueError("Lỗi: n phải lớn hơn 0.")


    s1 = tong_S1(n)
    s2 = tong_S2(n)

    print(f"S1 = 1 + 2 + ... + {n} = {s1}")
    print(f"S2 = 1^2 + 2^2 + ... + {n}^2 = {s2}")

except ValueError as loi:
    print(loi)

except RecursionError:
    print("Lỗi: Quá sâu trong đệ quy! n quá lớn.")

except Exception as loi_khac:
    print(f"Lỗi không xác định: {loi_khac}")
