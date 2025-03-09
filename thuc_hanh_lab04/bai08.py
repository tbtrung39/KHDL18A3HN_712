ky_tu = input("Nhập một ký tự bất kỳ là: ")
while len(ky_tu) != 1:
    print("Vui lòng nhập đúng một ký tự.")
    ky_tu = input("Nhập một ký tự: ")
print(f"Mã ASCII của '{ky_tu}' là {ord(ky_tu)}")