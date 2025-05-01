def ucln(a, b):
    return a if b == 0 else ucln(b, a % b)

def ucln_n(danh_sach, vi_tri = 0):
    if len(danh_sach) == 1:
        return danh_sach[0]
    if vi_tri == len(danh_sach) - 1:
        return danh_sach[vi_tri]
    return ucln(danh_sach[vi_tri], ucln_n(danh_sach, vi_tri + 1))

n = int(input("Nhập số lượng số: "))
ds = [int(input(f"Nhập số thứ {i + 1}: ")) for i in range(n)]
print("Ước chung lớn nhất là:", ucln_n(ds))