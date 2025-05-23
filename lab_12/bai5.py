# bai 5
def tong_s1(n):
    if n == 1:
        return 1
    else:
        return n + tong_s1(n - 1)
def tong_s2(n):
    if n == 1:
        return 1
    else:
        return n**2 + tong_s2(n - 1)

def nhap_n():
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if n <= 0:
            raise ValueError("Gia tri n phai la so nguyen duong.")
        return n
    except ValueError as e:
        raise ValueError(f"Gia tri n khong hop le: {e}")

def main():
    try:
        n = nhap_n()
        s1 = tong_s1(n)
        s2 = tong_s2(n)
        print(f"tong S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"tong S2 = 1 + 2^2 + ... + {n}^2 = {s2}")
    except Exception as e:
        print("loi:", e)

main()
