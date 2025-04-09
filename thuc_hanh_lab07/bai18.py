sinh_vien = {}
n = int(input("Nhap so sv:"))
for i in range(n):
    ma_sinh_vien = input("Nhap ma sv :")
    ten = input("Nhap ho ten: ")
    diem = float(input("Nhap diem: "))
    sinh_vien[ma_sinh_vien] = {"Ho va ten": ten,"Diem": diem}
ma_sv = input("Nhap so bao danh: ")
print(sinh_vien.get(ma_sv, "Khong tim thay sinh vien!!!"))