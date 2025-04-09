nv = {}
while True:
    print("\nMENU: ")
    chon = input("Chọn chức năng: ")
    if chon == 'a':
        ma = input("Mã NV: ")
        ten = input("Họ tên: ")
        ns = int(input("Năm sinh: "))
        luong = int(input("Lương: "))
        nv[ma] = [ten, ns, luong]
    elif chon == 'b':
        ma = input("Nhập mã: ")
        if ma in nv:
            print(nv[ma][0], nv[ma][1], nv[ma][2])
        else:
            print("Không tìm thấy")
    elif chon == 'c':
        ma = input("Mã tăng lương: ")
        if ma in nv:
            nv[ma][2] += 1000000
    elif chon == 'd':
        ma = input("Mã cần xóa: ")
        if ma in nv:
            del nv[ma]
    elif chon == 'e':
        print("Sắp xếp theo năm sinh:")
        for ma in sorted(nv, key=lambda x: nv[x][1]):
            print(ma, nv[ma][0], nv[ma][1], nv[ma][2])
    elif chon == 'f':
        break
