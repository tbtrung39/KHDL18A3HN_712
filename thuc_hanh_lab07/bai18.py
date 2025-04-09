# Từ điển ban đầu chứa thông tin thí sinh
thi_sinh = {
    "123456": {"ho_ten": "Nguyen Van A", "diem": 8.5},
    "654321": {"ho_ten": "Tran Thi B", "diem": 9.0},
    "111222": {"ho_ten": "Le Van C", "diem": 7.0}
}

sbd = input("Nhập số báo danh: ")

if sbd in thi_sinh:
    print("Thông tin thí sinh:")
    print("Họ và tên:", thi_sinh[sbd]["ho_ten"])
    print("Điểm thi:", thi_sinh[sbd]["diem"])
else:
    print("Không có thí sinh này. Hãy nhập thêm thông tin:")
    ho_ten = input("Nhập họ và tên: ")
    diem = float(input("Nhập điểm thi: "))
    thi_sinh[sbd] = {"ho_ten": ho_ten, "diem": diem}
    print("Đã thêm thí sinh mới vào danh sách.")
print("\nDanh sách thí sinh hiện tại:")
for ma_sbd, thong_tin in thi_sinh.items():
    print(f"{ma_sbd}: {thong_tin['ho_ten']}, {thong_tin['diem']} điểm")