
def tong_de_quy(n):
    if n == 1:
        return 1
    return n + tong_de_quy(n - 1)
def tong_binh_phuong_de_quy(n):
    if n == 1:
        return 1
    return n**2 + tong_binh_phuong_de_quy(n - 1)
def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            raise ValueError("n phải là số nguyên dương lớn hơn 0.")
        s1 = tong_de_quy(n)
        s2 = tong_binh_phuong_de_quy(n)
        print(f"Tổng S1 = {s1}")
        print(f"Tổng S2 = {s2}")
    except ValueError as loi:
        print(f"Lỗi: {loi}")
if __name__ == "__main__":
    main()
