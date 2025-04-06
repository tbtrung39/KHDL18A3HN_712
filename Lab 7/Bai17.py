#Bai17
sinh_vien = []
while True:
    ma_sinh_vien = input("Nhập mã sinh viên (06 ký tự): ")
    if ma_sinh_vien == " ":
        break
    ho_ten = input("Nhập họ tên sinh viên: ")
    chuoi_diem = input("Nhập điểm (0-10): ")
    if chuoi_diem.replace('.', '', 1).isdigit():
        diem = round(float(chuoi_diem))
        if diem < 0 or diem > 10:
            print("Điểm nhập vào không hợp lệ!")
        else:
            sinh_vien.append({
                "ma_sinh_vien": ma_sinh_vien,
                "ho_ten": ho_ten,
                "diem": diem
            })
    else:
        print("Điểm nhập vào không hợp lệ!")
n = len(sinh_vien)
for i in range(n - 1):
    for j in range(n - i - 1):
        if sinh_vien[j]["diem"] < sinh_vien[j + 1]["diem"]:
            sinh_vien[j], sinh_vien[j + 1] = sinh_vien[j + 1], sinh_vien[j]
print()
print("--------------------THÔNG TIN SINH VIÊN--------------------")
print("*" * 60)
print("Mã SV".ljust(8), "Họ tên".ljust(30), "Điểm".rjust(5))
print("-" * 60)
for sv in sinh_vien:
    print(sv["ma_sinh_vien"].ljust(8),
          sv["ho_ten"].ljust(30),
          str(sv["diem"]).rjust(5))