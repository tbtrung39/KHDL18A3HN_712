char = input("Nhập một ký tự: ")
while len(char) != 1:
    print("Vui lòng nhập đúng một ký tự!")
    char = input("Nhập một ký tự: ")
ascii_value = ord(char)
print(f"Giá trị ASCII của '{char}' là: {ascii_value}")