#Bai15
def list_songuyen(n):
    lst = []
    for i in range(n):
        m = int(input(f"Nhap phan tu thu {i+1}:"))
        lst.append(m)
    return lst
def binh_phuong_so_le(lst):
    return list(map(lambda m: m**2, filter(lambda m: m % 2 != 0, lst)))
n = int(input("Nhap so phan tu: "))
ds = list_songuyen(n)
kq = binh_phuong_so_le(ds)
print("List binh phuong cac so le:", kq)