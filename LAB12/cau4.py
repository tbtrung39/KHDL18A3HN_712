try:
    path = input("Nhập đường dẫn file: ")
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        print("Nội dung file:")
        print(data)
except FileNotFoundError:
    print("Lỗi: File không tồn tại.")
except PermissionError:
    print("Lỗi: Không có quyền truy cập file.")
except Exception as e:
    print("Lỗi khác:", e)