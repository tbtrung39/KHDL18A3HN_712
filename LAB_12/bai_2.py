try:
    filename = input("Nhập tên tệp: ")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Nội dung tệp:\n", content)
except FileNotFoundError:
    print("Tệp không tồn tại.")