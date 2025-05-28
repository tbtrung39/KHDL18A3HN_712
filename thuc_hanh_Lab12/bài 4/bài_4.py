try:
    ten_tep_nguon = input("Nhập tên tập tin cần đọc: ")
    ten_tep_dich = input("Nhập tên tập tin để ghi vào: ")
    f_in = open(ten_tep_nguon, 'r', encoding='utf-8')

    noi_dung = f_in.read()

    f_out = open("bài 4/" + ten_tep_dich, 'w', encoding='utf-8')
    f_out.write(noi_dung)
    print("Đã sao chép nội dung vào file mới thành công.")
    f_in.close()
    f_out.close()
except FileNotFoundError:
    print(" Lỗi: Không tìm thấy tập tin nguồn.")
except IOError:
    print(" Lỗi: Không thể đọc hoặc ghi file.")
