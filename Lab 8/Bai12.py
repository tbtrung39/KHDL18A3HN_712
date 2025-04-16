#Bai12
def nhap_thong_tin_nv():
    hoten = input("Ho ten nhan vien: ")
    que_quan = input("Que quan nhan vien: ")
    tham_nien_cong_tac = int(input("Tham nien cong tac: "))
    return hoten, que_quan, tham_nien_cong_tac
def tinh_luong(tham_nien_cong_tac):
    luong_moi_nam = int(input("Nhap muc luong moi nam: "))
    return tham_nien_cong_tac * luong_moi_nam
def xuat_thong_tin_nv(hoten, que_quan, tham_nien_cong_tac, luong):
    print("----------------THONG TIN NHAN VIEN----------------")
    print("Ho ten:", hoten)
    print("Que quan:", que_quan)
    print("Tham nien cong tac:", tham_nien_cong_tac)
    print("Luong:", luong, "VND")
hoten, que_quan, tham_nien_cong_tac = nhap_thong_tin_nv()
luong = tinh_luong(tham_nien_cong_tac)
xuat_thong_tin_nv(hoten, que_quan, tham_nien_cong_tac, luong)