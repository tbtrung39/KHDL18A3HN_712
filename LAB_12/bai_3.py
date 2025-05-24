try:
    input_file = input("Nhập tên tệp cần đọc: ")
    output_file = input("Nhập tên tệp ghi ra: ")

    with open(input_file, 'r', encoding='utf-8') as f1:
        content = f1.read()

    with open(output_file, 'w', encoding='utf-8') as f2:
        f2.write(content)

    print("Ghi nội dung thành công.")

except FileNotFoundError:
    print("Tệp nguồn không tồn tại.")
except IOError as e:
    print("Lỗi xử lý tệp:", e)