ten_file = input("Nhập tên file để đọc: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("Đã ghi nội dung vào output.txt")
except FileNotFoundError:
    print("Lỗi: File không tồn tại")
except IOError:
    print("Lỗi: Chế độ mở file không đúng")