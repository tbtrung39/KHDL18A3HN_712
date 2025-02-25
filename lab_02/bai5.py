ky_tu = input("Nhập một ký tự: ")
if ky_tu.isalpha() and len(ky_tu) == 1:
    ky_tu = ky_tu.lower()
    if ky_tu in 'aeiou':
        print(f"{ky_tu} là nguyên âm.")
    else:
        print(f"{ky_tu} là phụ âm.")
else:
    print("Vui lòng nhập một ký tự hợp lệ (chỉ một ký tự chữ cái).")
