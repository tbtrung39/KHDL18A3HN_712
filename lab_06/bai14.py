# Nhập mật khẩu từ bàn phím
password = input("Nhập mật khẩu: ")

# Kiểm tra độ dài mật khẩu
if 6 <= len(password) <= 12:
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    # Duyệt từng ký tự trong mật khẩu
    for char in password:
        if 'a' <= char <= 'z':  # Chữ thường
            co_chu_thuong = True
        elif 'A' <= char <= 'Z':  # Chữ hoa
            co_chu_hoa = True
        elif '0' <= char <= '9':  # Số
            co_so = True
        elif char in "$#@":  # Ký tự đặc biệt
            co_ky_tu_dac_biet = True

    # Kiểm tra xem mật khẩu có đủ 4 điều kiện không
    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu không hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
