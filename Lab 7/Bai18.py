#Bai18
thi_sinh = []
while True:
    so_bao_danh = input("Nhập số báo danh (số 6 ký tự): ")
    if so_bao_danh == "":
        break
    for ts in thi_sinh:
        if ts["so_bao_danh"] == so_bao_danh:
            print("Số báo danh", so_bao_danh, "tồn tại với tên", ts["ho_ten"], "và điểm", ts["diem_thi"])
            break
    else:
        ho_ten = input(" Nhập họ và tên thí sinh: ")
        diem_thi = int(input("Nhập điểm thi (0-10): "))
        thi_sinh.append({
            "so_bao_danh": so_bao_danh,
            "ho_ten": ho_ten,
            "diem_thi": diem_thi
        })
        print(" Thêm thí sinh thành công!")

print("------------------DANH SÁCH THÍ SINH------------------")
print("="*50)
print("SBD".ljust(10), "Họ và tên".ljust(25), "Điểm thi".rjust(10))
print("="*50)
for ts in thi_sinh:
    print(ts["so_bao_danh"].ljust(10), ts["ho_ten"].ljust(25), str(ts["diem_thi"]).rjust(10))