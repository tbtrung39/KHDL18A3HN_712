nhan_vien_dict = {}
while True:
    print("\nChọn chức năng:")
    print("1. Tạo mới từ điển")
    print("2. Thêm nhân viên")
    print("3. Tìm kiếm nhân viên theo mã")
    print("4. Tăng lương cho nhân viên")
    print("5. Xóa nhân viên")
    print("6. Sắp xếp nhân viên theo năm sinh giảm dần")
    print("7. Thoát")

    chon = input("Lựa chọn: ")
    if chon == '1':
        nhan_vien_dict = {}
        print("Từ điển đã được tạo mới!")
    elif chon == '2':
        ma_nhan_vien = input("Nhập mã nhân viên (4 ký tự số): ")
        ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
        nam_sinh = int(input("Nhập năm sinh nhân viên: "))
        luong = float(input("Nhập lương nhân viên: "))
        nhan_vien_dict[ma_nhan_vien] = [ho_ten, nam_sinh, luong]
        print("Thông tin nhân viên đã được thêm!")
    elif chon == '3':
        ma_nhan_vien = input("Nhập mã nhân viên để tìm kiếm: ")
        if ma_nhan_vien in nhan_vien_dict:
            print(f"Thông tin nhân viên {ma_nhan_vien}: {nhan_vien_dict[ma_nhan_vien]}")
        else:
            print("Mã nhân viên không tồn tại!")
    elif chon == '4':
        ma_nhan_vien = input("Nhập mã nhân viên để tăng lương: ")
        if ma_nhan_vien in nhan_vien_dict:
            nhan_vien_dict[ma_nhan_vien][2] += 1000000  # Tăng lương
            print(f"Lương của nhân viên {ma_nhan_vien} đã được tăng thêm 1,000,000!")
        else:
            print("Mã nhân viên không tồn tại!")
    elif chon == '5':
        ma_nhan_vien = input("Nhập mã nhân viên để xóa: ")
        if ma_nhan_vien in nhan_vien_dict:
            del nhan_vien_dict[ma_nhan_vien]
            print(f"Nhân viên {ma_nhan_vien} đã được xóa!")
        else:
            print("Mã nhân viên không tồn tại!")
    elif chon == '6':
        danh_sach_ma_nv = list(nhan_vien_dict.keys())
        for i in range(len(danh_sach_ma_nv) - 1):
            for j in range(i + 1, len(danh_sach_ma_nv)):
                ma1, ma2 = danh_sach_ma_nv[i], danh_sach_ma_nv[j]
                if nhan_vien_dict[ma1][1] < nhan_vien_dict[ma2][1]:
                    danh_sach_ma_nv[i], danh_sach_ma_nv[j] = danh_sach_ma_nv[j], danh_sach_ma_nv[i]
        print("Danh sách nhân viên sắp xếp theo năm sinh giảm dần:")
        for ma_nhan_vien in danh_sach_ma_nv:
            print(f"Mã nhân viên: {ma_nhan_vien}, Thông tin: {nhan_vien_dict[ma_nhan_vien]}")
    elif chon == '7':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")