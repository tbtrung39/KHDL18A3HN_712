nhan_vien = {}
while True:
    print("\nChọn thao tác:")
    print("1. Thêm nhân viên")
    print("2. Tìm kiếm nhân viên")
    print("3. Tăng lương nhân viên")
    print("4. Xóa nhân viên")
    print("5. Sắp xếp theo năm sinh")
    print("6. In từ điển")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn: ")

    if lua_chon == '1':
        ma_nv = input("Nhập mã nhân viên (4 ký tự số): ")
        if not ma_nv.isdigit() or len(ma_nv) != 4:
            print("Mã nhân viên không hợp lệ.")
            continue
        ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
        if len(ho_ten) > 20:
            print("Họ tên quá dài.")
            continue
        nam_sinh = int(input("Nhập năm sinh: "))
        luong = int(input("Nhập lương: "))
        nhan_vien[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}
        print("Đã thêm nhân viên.")

    elif lua_chon == '2':
        ma_nv_tim = input("Nhập mã nhân viên cần tìm: ")
        if ma_nv_tim in nhan_vien:
            print("Thông tin nhân viên:")
            print(f"Mã NV: {ma_nv_tim}, Họ tên: {nhan_vien[ma_nv_tim]['ho_ten']}, Năm sinh: {nhan_vien[ma_nv_tim]['nam_sinh']}, Lương: {nhan_vien[ma_nv_tim]['luong']}")
        else:
            print("Không tìm thấy nhân viên.")

    elif lua_chon == '3':
        ma_nv_tang_luong = input("Nhập mã nhân viên cần tăng lương: ")
        if ma_nv_tang_luong in nhan_vien:
            nhan_vien[ma_nv_tang_luong]['luong'] += 1000000
            print("Đã tăng lương.")
        else:
            print("Không tìm thấy nhân viên.")

    elif lua_chon == '4':
        ma_nv_xoa = input("Nhập mã nhân viên cần xóa: ")
        if ma_nv_xoa in nhan_vien:
            del nhan_vien[ma_nv_xoa]
            print("Đã xóa nhân viên.")
        else:
            print("Không tìm thấy nhân viên.")

    elif lua_chon == '5':
        danh_sach_nv_sap_xep = sorted(nhan_vien.items(), key=lambda x: x[1]['nam_sinh'], reverse=True)
        print("Danh sách nhân viên theo năm sinh giảm dần:")
        for ma_nv, thong_tin in danh_sach_nv_sap_xep:
            print(f"Mã NV: {ma_nv}, Họ tên: {thong_tin['ho_ten']}, Năm sinh: {thong_tin['nam_sinh']}, Lương: {thong_tin['luong']}")

    elif lua_chon == '6':
        print("\nThông tin nhân viên:")
        for ma_nv, thong_tin in nhan_vien.items():
            print(f"Mã NV: {ma_nv}, Họ tên: {thong_tin['ho_ten']}, Năm sinh: {thong_tin['nam_sinh']}, Lương: {thong_tin['luong']}")
    elif lua_chon == '0':
        break
    else:
        print("Lựa chọn không hợp lệ.")