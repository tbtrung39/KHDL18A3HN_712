# bai 4
def sao_chep_file():
    f_nguon = None
    f_dich = None
    try:
        ten_file_nguon = input("Nhap ten tap tin can doc tu ban phim: ")
        ten_file_dich = input("Nhap ten tap tin moi de ghi: ")
        f_nguon = open(ten_file_nguon, "r", encoding="utf-8")

        f_dich = open(ten_file_dich, "w", encoding="utf-8")

        noi_dung = f_nguon.read()
        f_dich.write(noi_dung)

        print(f"Da sao chep noi dung vao tap tin '{ten_file_dich}'.")

    except Exception as e:
        print("Loi mo file hoac ghi file:", e)
    finally:
        if f_nguon:
            f_nguon.close()
        if f_dich:
            f_dich.close()
sao_chep_file()
