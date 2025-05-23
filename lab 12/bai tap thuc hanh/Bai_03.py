def sao_chep_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r', encoding='utf-8') as file_goc:
            noi_dung = file_goc.read()

        with open("copy.dat", 'w', encoding='utf-8') as file_copy:
            file_copy.write(noi_dung)

        print("Đã sao chép nội dung vào tập tin thành công.")

    except FileNotFoundError as f:
        print("Lỗi",f)
    except Exception as e:
        print("Lỗi:", e)

ten_file = input("Nhập tên tập tin cần đọc: ")
sao_chep_tap_tin(ten_file)
