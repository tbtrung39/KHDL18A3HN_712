print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
print("0. Thoát")
lua_chon = -1 
while lua_chon != 0:
    lua_chon = int(input("Nhập đồ uống bạn muốn chọn hoặc 0 = thoát: "))
    if lua_chon == 1:
        print("Bạn đã chọn Cafe.")
    elif lua_chon == 2:
        print("Bạn đã chọn Cam vắt.")
    elif lua_chon == 3:
        print("Bạn đã chọn Nước ép cà rốt.")
    elif lua_chon == 4:
        print("Bạn đã chọn Nước lọc.")
    elif lua_chon == 5:
        print("Bạn đã chọn Nước dừa.")
    elif lua_chon == 0:
        print("Cảm ơn bạn đã sử dụng dịch vụ!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")