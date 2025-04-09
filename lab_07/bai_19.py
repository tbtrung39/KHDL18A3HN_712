nhan_vien = {}
while True:
    print("\nChon thao tac:")
    print("1. Them nhan vien")
    print("2. Tim kiem nhan vien")
    print("3. Tang luong nhan vien")
    print("4. Xoa nhan vien")
    print("5. Sap xep theo nam sinh")
    print("6. In tu dien")
    print("0. Thoat")

    lua_chon = input("Nhap lua chon: ")

    if lua_chon == '1':
        ma_nv = input("Nhap ma nhan vien (4 ky tu so): ")
        if not ma_nv.isdigit() or len(ma_nv) != 4:
            print("Ma nhan vien khong hop le.")
            continue
        ho_ten = input("Nhap ho ten nhan vien (toi đa 20 ky tu): ")
        if len(ho_ten) > 20:
            print("Ho ten qua dai.")
            continue
        nam_sinh = int(input("Nhap nam sinh: "))
        luong = int(input("Nhap luong: "))
        nhan_vien[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}
        print("Đa them nhan vien.")

    elif lua_chon == '2':
        ma_nv_tim = input("Nhap ma nhan vien can tim: ")
        if ma_nv_tim in nhan_vien:
            print("Thong tin nhan vien:")
            print(f"Ma NV: {ma_nv_tim}, Ho ten: {nhan_vien[ma_nv_tim]['ho_ten']}, Nam sinh: {nhan_vien[ma_nv_tim]['nam_sinh']}, Luong: {nhan_vien[ma_nv_tim]['luong']}")
        else:
            print("Khong tim thay nhan vien.")

    elif lua_chon == '3':
        ma_nv_tang_luong = input("Nhap ma nhan vien can tang luong: ")
        if ma_nv_tang_luong in nhan_vien:
            nhan_vien[ma_nv_tang_luong]['luong'] += 1000000
            print("Da tang luong.")
        else:
            print("Khong tim thay nhan vien.")

    elif lua_chon == '4':
        ma_nv_xoa = input("Nhap ma nhan vien can xoa: ")
        if ma_nv_xoa in nhan_vien:
            del nhan_vien[ma_nv_xoa]
            print("Da xoa nhan vien.")
        else:
            print("Khong tim thay nhan vien.")

    elif lua_chon == '5':
        danh_sach_nv_sap_xep = sorted(nhan_vien.items(), key=lambda x: x[1]['nam_sinh'], reverse=True)
        print("Danh sach nhan vien theo nam sinh giam dan:")
        for ma_nv, thong_tin in danh_sach_nv_sap_xep:
            print(f"Ma NV: {ma_nv}, Ho ten: {thong_tin['ho_ten']}, Nam sinh: {thong_tin['nam_sinh']}, Luong: {thong_tin['luong']}")

    elif lua_chon == '6':
        print("\nThong tin nhan vien:")
        for ma_nv, thong_tin in nhan_vien.items():
            print(f"Ma NV: {ma_nv}, Ho ten: {thong_tin['ho_ten']}, Nam sinh: {thong_tin['nam_sinh']}, Luong: {thong_tin['luong']}")
    elif lua_chon == '0':
        break
    else:
        print("Lua chon khong hop le.")