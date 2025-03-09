char = input("Nhập một ký tự: ")

while len(char) != 1:
    print("Vui lòng nhập đúng một ký tự.")
    char = input("Nhập một ký tự: ")

print(f"Mã ASCII của '{char}' là {ord(char)}")
