try:
    file_name = input("Nhập tên tập tin văn bản: ")
    with open(file_name, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    with open("bài 3/copy.dat", 'w', encoding='utf-8') as f_out:
       
        f_out.write(content)
    print("Đã sao chép nội dung vào file copy.dat")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin.")
