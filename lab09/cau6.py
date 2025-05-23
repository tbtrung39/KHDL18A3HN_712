import random

def sinh_hoan_vi_ngau_nhien(n):
    if not isinstance(n, int) or n <= 0:
        return "Vui long nhap mot so tu nhien duong."

    danh_sach = list(range(1, n + 1))
    hoan_vi = []

    for _ in range(n):
        vi_tri = random.randrange(len(danh_sach)) 
        gia_tri = danh_sach.pop(vi_tri)
        hoan_vi.append(gia_tri)

    return hoan_vi

try:
    so_n = int(input("Nhap mot so tu nhien n: "))
    ket_qua = sinh_hoan_vi_ngau_nhien(so_n)
    print(f"Mot hoan vi ngau nhien cua cac so tu 1 den {so_n} la: {ket_qua}")
except ValueError:
    print("Dau vao khong hop le. Vui long nhap mot so nguyen.")