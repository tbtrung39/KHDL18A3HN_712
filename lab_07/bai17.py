sinh_vien_dict = {}
n = int(input("Nhập số lượng sinh viên: "))
for _ in range(n):
    ma_sinh_vien = input("Nhập mã sinh viên (6 ký tự số): ")
    ten_sinh_vien = input("Nhập tên sinh viên: ")
    diem_sinh_vien = int(input("Nhập điểm sinh viên (0-10): "))
    if diem_sinh_vien < 0:
        diem_sinh_vien = 0
    elif diem_sinh_vien > 10:
        diem_sinh_vien = 10
    sinh_vien_dict[ma_sinh_vien] = (ten_sinh_vien, diem_sinh_vien)
sorted_sinh_vien = sorted(sinh_vien_dict, key=lambda ma_sv: sinh_vien_dict[ma_sv][1], reverse=True)
print("\nDanh sách sinh viên theo điểm giảm dần:")
for ma_sv in sorted_sinh_vien:
    ten_sv, diem_sv = sinh_vien_dict[ma_sv]
    print(f"Mã sinh viên: {ma_sv}, Tên sinh viên: {ten_sv}, Điểm: {diem_sv}")