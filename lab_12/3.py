ten_file = input("Nhập tên file: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("copy.dat", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("Đã sao chép nội dung vào copy.dat")
except FileNotFoundError:
    print("Không tìm thấy file")
    exit()