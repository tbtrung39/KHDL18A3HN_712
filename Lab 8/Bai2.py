#Bai2
#a.Tìm UCLN của tử số và mẫu số
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#b.Rút gọn phân số
def rut_gon(tu, mau):
    uoc_chung = ucln(tu, mau)
    tu_so_rut_gon = tu // uoc_chung
    mau_so_rut_gon = mau // uoc_chung
    return tu_so_rut_gon, mau_so_rut_gon
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
if mau_so == 0:
    print("Nhập sai, vui lòng nhập lại!")
else:
    tu_moi, mau_moi = rut_gon(tu_so, mau_so)
    print("Phân số sau khi rút gọn:", tu_moi, "/", mau_moi)