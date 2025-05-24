def sao_chep_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r', encoding='utf-8') as file_goc:
            noi_dung = file_goc.read()

        with open("copy.dat", 'w', encoding='utf-8') as file_copy:
            file_copy.write(noi_dung)

        print("Da sao chep noi dung vao tap tin thanh cong.")

    except FileNotFoundError as f:
        print("Loi",f)
    except Exception as e:
        print("Loi:", e)

ten_file = input("Nhap ten tap tin can doc: ")
sao_chep_tap_tin(ten_file)