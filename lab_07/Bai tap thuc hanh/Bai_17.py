sinh_vien = {}
while True:
    ma_sv = input("Nhập mã sinh viên (6 ký tự số, hoặc 'done' để kết thúc): ")
    if ma_sv.lower() == 'done':
        break

    if not ma_sv.isdigit() or len(ma_sv) != 6:
        print("Mã sinh viên không hợp lệ. Vui lòng nhập lại.")
        continue

    ten_sv = input("Nhập tên sinh viên: ")
    try:
        diem_sv = int(round(float(input("Nhập điểm sinh viên: "))))
        if not 0 <= diem_sv <= 10:
            raise ValueError
    except ValueError:
        print("Điểm không hợp lệ. Vui lòng nhập lại.")
        continue

    sinh_vien[ma_sv] = {"ten": ten_sv, "diem": diem_sv}

danh_sach_sv = list(sinh_vien.items())
danh_sach_sv.sort(key=lambda x: x[1]["diem"], reverse=True)
print("\nDanh sách sinh viên theo điểm giảm dần:")
for ma_sv, thong_tin in danh_sach_sv:
    print(f"Mã SV: {ma_sv}, Tên: {thong_tin['ten']}, Điểm: {thong_tin['diem']}")