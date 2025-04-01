import re
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    if not re.search(r'[a-z]', password):  # Ít nhất 1 chữ cái thường
        return False
    if not re.search(r'[0-9]', password):  # Ít nhất 1 số
        return False
    if not re.search(r'[A-Z]', password):  # Ít nhất 1 chữ cái hoa
        return False
    if not re.search(r'[@#$]', password):  # Ít nhất 1 ký tự đặc biệt
        return False

    return True


password = input("Nhập mật khẩu: ")

if check_password(password):
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")
