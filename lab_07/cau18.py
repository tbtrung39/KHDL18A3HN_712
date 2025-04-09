sv = {}
n = int(input("Nhap so sv:"))
for i in range(n):
    ma_sv = input("Nhap ma sv :")
    ten = input("Nhap ho ten: ")
    diem = float(input("Nhap diem: "))
    sv[ma_sv] = {"Ho va ten": ten,"Diem": diem}
ma_sv = input("Nhap so bao danh: ")
print(sv.get(ma_sv, "Khong tim thay sinh vien!!!"))