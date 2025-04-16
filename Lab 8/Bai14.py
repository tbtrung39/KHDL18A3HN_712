#Bai14
def tao_list_songuyen():
    n = int(input("Nhap so phan tu: "))
    lst = []
    for i in range(n):
        m = int(input(f"Nhap phan tu thu {i+1}:"))
        lst.append(m)
    lst_binh_phuong = list(map(lambda m: m**2, lst))
    print("List chua binh phuong:", lst_binh_phuong)
tao_list_songuyen()