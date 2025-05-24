ten_file = input("nhap file: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("copy.dat", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("da sao chep noi dung")
except FileNotFoundError:
    print("khong tim thay file")
    exit()