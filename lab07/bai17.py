sv = {}
n = int(input("Nhap so sinh vien: "))
for _ in range(n):
    ma_sinh_vien = input("Nhap ma sinh vien(6 ky tu): ")
    ten_sinh_vien = input("Nhap ten sinh vien: ")
    diem_sinh_vien = int(input("Nhap diem(0-10): "))
    if diem_sinh_vien < 0:
        diem_sinh_vien = 0
    elif diem_sinh_vien > 10:
        diem_sinh_vien = 10
    sv[ma_sinh_vien] = (ten_sinh_vien, diem_sinh_vien)
sorted_sinh_vien = sorted(sv, key=lambda ma_sv: sv[ma_sv][1], reverse=True)
print("\nDanh sach sv theo diem giam dan: ")
for ma_sv in sorted_sinh_vien:
    ten_sv, diem_sv = sv[ma_sv]
    print(f"Ma sinh vien: {ma_sv}, Ten sinh vien: {ten_sv}, Diem: {diem_sv}")