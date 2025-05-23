def sao_chep_tap_tin(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f_nguon:
            noi_dung = f_nguon.read()

        with open('copy_c4.dat', 'w', encoding='utf-8') as f_dich:
            f_dich.write(noi_dung)

        print("Sao chép tập tin thành công sang 'copy_c4.txt'!")

    except FileNotFoundError:
        print("Lỗi: Tập tin nguồn không tồn tại.")
    except IOError:
        print("Lỗi: Không thể đọc hoặc ghi tập tin.")
    except Exception as e:
        print("Lỗi không xác định:", e)
ten_file = input("Nhập tên tập tin cần đọc: ")
sao_chep_tap_tin(ten_file)
