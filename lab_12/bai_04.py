ten_file = input("Nhap ten file: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("Da ghi noi dung")
except FileNotFoundError:
    print("Khong tim thay file")
except IOError:
    print("Loi mo file")