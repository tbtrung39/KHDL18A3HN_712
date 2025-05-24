try:
    ten_tap_tin = input("Nhập tên tập tin cần đọc: ")
    with open(ten_tap_tin, 'r', encoding='utf-8') as tep_nguon:
        noi_dung = tep_nguon.read()

    with open('copy.dat', 'w', encoding='utf-8') as tep_dich:
        tep_dich.write(noi_dung)

    print("Đã sao chép nội dung sang tập tin 'copy.dat'.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin với tên vừa nhập.")

except Exception as loi:
    print(f"Đã xảy ra lỗi: {loi}")
