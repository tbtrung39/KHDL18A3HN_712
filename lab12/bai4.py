ten_file = input("nhap ten file: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("da ghi noi dung")
except FileNotFoundError:
    print("khong tim thay file")
except IOError:
    print("loi mo file")