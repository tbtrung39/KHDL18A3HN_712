try:
    ten_tep_vao = input("Nhập tên tập tin nguồn: ")
    ten_tep_ra = input("Nhập tên tập tin đích: ")
    
    with open(ten_tep_vao, 'r', encoding='utf-8') as file_in:
        noi_dung = file_in.read()

    with open(ten_tep_ra, 'w', encoding='utf-8') as file_out:
        file_out.write(noi_dung)

    print("Ghi dữ liệu thành công.")
except FileNotFoundError:
    print("Không tìm thấy tập tin nguồn.")
except IOError:
    print("Lỗi đọc/ghi tập tin.")
except Exception as e:
    print("Lỗi khác:", e)
finally:
    print("Kết thúc chương trình và đóng tệp.")