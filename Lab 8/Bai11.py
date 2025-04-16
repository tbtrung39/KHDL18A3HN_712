#Bai11
def tinh_diem_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def nhap_thong_tin():
    hoten = input("Ho ten: ")
    toan = float(input("Nhap diem toan: "))
    ly = float(input("Nhap diem ly: "))
    hoa = float(input("Nhap diem hoa: "))
    return hoten, toan, ly, hoa
def in_thong_tin(hoten, diem_tb):
    print(hoten, "co diem trung binh la:", diem_tb)
hoten, toan, ly, hoa = nhap_thong_tin()
diem_tb = tinh_diem_tb(toan, ly, hoa)
in_thong_tin(hoten, diem_tb)