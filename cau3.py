def sao_chep_tep_tin(ten_tep):
    try:
        with open(ten_tep, 'r', encoding='utf-8') as tep_goc, \
             open('copy.dat', 'w', encoding='utf-8') as tep_moi:
            tep_moi.write(tep_goc.read())
        print("Đã sao chép nội dung sang file 'copy.dat' thành công.")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tập tin.")
    except Exception as e:
        print(f"Lỗi khi sao chép: {e}")

ten_file = input("Nhập tên tập tin cần đọc: ")
sao_chep_tep_tin(ten_file)
