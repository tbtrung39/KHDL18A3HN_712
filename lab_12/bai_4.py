try:
    ten_tep_nguon = input("Nhập tên tập tin cần đọc: ")

    tep_nguon = open(ten_tep_nguon, 'r', encoding='utf-8')
 
    noi_dung = tep_nguon.read()

    ten_tep_dich = input("Nhập tên tập tin để ghi nội dung vào: ")
    
    tep_dich = open(ten_tep_dich, 'w', encoding='utf-8')

    tep_dich.write(noi_dung)

    print(f"Đã sao chép nội dung từ '{ten_tep_nguon}' sang '{ten_tep_dich}'.")

except FileNotFoundError:
    print("Lỗi: Tập tin không tồn tại.")

except IOError:
    print("Lỗi: Không thể đọc hoặc ghi tập tin. Có thể mở sai chế độ.")

except Exception as loi_chung:
    print(f"Lỗi không xác định: {loi_chung}")

finally:
    try:
        tep_nguon.close()
    except:
        pass
    try:
        tep_dich.close()
    except:
        pass
