# bai 3
def doc_va_sao_chep_file():
    try:
        ten_file = input("Nhap ten tap tin can doc: ")
        with open(ten_file, "r", encoding="utf-8") as f:
            noi_dung = f.read()
        with open("copy.dat", "w", encoding="utf-8") as f_copy:
            f_copy.write(noi_dung)
        print("da sao chep noi dung vao file 'copy.dat'.")

    except FileNotFoundError:
        print("loi, tap tin ko ton tai")

doc_va_sao_chep_file()

