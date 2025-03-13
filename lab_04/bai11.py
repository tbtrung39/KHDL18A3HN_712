while True:
    print("\n--- Menu đồ uống ---")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("0. Thoát")

    lua_chon = input("Nhập số để chọn đồ uống: ")

    if lua_chon == "1":
        print("Bạn đã chọn Cafe ")
    elif lua_chon == "2":
        print("Bạn đã chọn Cam vắt ")
    elif lua_chon == "3":
        print("Bạn đã chọn Nước ép cà rốt ")
    elif lua_chon == "0":
        print("Cảm ơn, hẹn gặp lại! ")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")