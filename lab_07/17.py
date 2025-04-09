ds_sinhvien = {}
while True:
    ma_sv = input("Nhập mã sinh viên (6 ký tự, hoặc 'q' để thoát): ")
    if ma_sv == 'q':
        break
    ho_ten = input("Nhập họ và tên: ")
    diem = float(input("Nhập điểm (0 đến 10): "))
    ds_sinhvien[ma_sv] = [ho_ten, diem]
print("\nDanh sách sinh viên theo điểm giảm dần:")
for sv in sorted(ds_sinhvien.items(), key=lambda x: x[1][1], reverse=True):
    print(f"MSSV: {sv[0]}, Họ tên: {sv[1][0]}, Điểm: {sv[1][1]}")
