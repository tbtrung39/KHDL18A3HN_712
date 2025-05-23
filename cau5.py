class LoiNhapSo(Exception):
    pass
def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_S2(n - 1)

try:
    n = input("Nhập n: ")
    if not n.isdigit():
        raise LoiNhapSo("Phải nhập một số nguyên dương!")
    n = int(n)
    if n <= 0:
        raise LoiNhapSo("n phải lớn hơn 0!")
    s1 = tinh_S1(n)
    s2 = tinh_S2(n)
    print(f"S1 = 1 + 2 + ... + {n} = {s1}")
    print(f"S2 = 1² + 2² + ... + {n}² = {s2}")
except LoiNhapSo as e:
    print("Lỗi nhập:", e)
except RecursionError:
    print("Lỗi đệ quy quá sâu. Giá trị n quá lớn!")
except Exception as e:
    print("Lỗi không xác định:", e)

    