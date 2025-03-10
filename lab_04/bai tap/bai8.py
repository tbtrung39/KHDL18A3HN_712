while True:
    ky_tu = input("Nhập một ký tự: ")
    if len(ky_tu) == 1:  # Chỉ chấp nhận một ký tự
        print(f"Giá trị ASCII của '{ky_tu}' là {ord(ky_tu)}")
        break
    else:
        print("Vui lòng nhập đúng một ký tự!")
