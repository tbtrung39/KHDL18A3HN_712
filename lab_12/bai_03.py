ten_file = input("Nhap file: ")
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    with open("copy.dat", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("Da sao chep noi dung")
except FileNotFoundError:
    print("Khong tim thay file")
    exit()