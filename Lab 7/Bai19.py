# Bai19
nhan_vien = {}
while True:
    print("\nMenu:")
    print("1. Tạo mới từ điển")
    print("2. Thêm nhân viên")
    print("3. Tìm kiếm nhân viên")
    print("4. Tăng lương")
    print("5. Xóa nhân viên")
    print("6. Sắp xếp giảm dần theo năm sinh")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")
    if chon == "1":
        nhan_vien = {} 
        print("Từ điển đã được tạo.")
    elif chon == "2":
        ma_nv = input("Nhập mã nhân viên (tối đa 4 ký tự): ")
        ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
        nam_sinh = int(input("Nhập năm sinh: "))
        luong = int(input("Nhập lương: "))
        nhan_vien[ma_nv] = {"Họ tên": ho_ten[:20], "năm sinh": nam_sinh, "lương": luong}
        print("Hoàn thành việc thêm nhân viên.")
    elif chon == "3":
        ma_nv = input("Nhập mã nhân viên cần tìm: ")
        if ma_nv in nhan_vien:
            print("Thông tin nhân viên:", nhan_vien[ma_nv])
        else:
            print("Không tìm thấy nhân viên.")
    elif chon == "4":
        ma_nv = input("Nhập mã nhân viên cần tăng lương: ")
        if ma_nv in nhan_vien:
            nhan_vien[ma_nv]["lương"] += 1000000
            print(f"Đã tăng lương. Lương mới: {nhan_vien[ma_nv]['lương']}")
        else:
            print("Không tìm thấy nhân viên.")
    elif chon == "5":
        ma_nv = input("Nhập mã nhân viên cần xóa: ")
        if ma_nv in nhan_vien:
            moi={}
            for k,v in nhan_vien.items():
                if k != ma_nv:
                    moi[k]=v
            nhan_vien=moi
            print("Đã xóa nhân viên.")
        else:
            print("Không tìm thấy nhân viên.")
    elif chon == "6":
        kq_nv = list(nhan_vien.items())
        for i in range(len(kq_nv)):
            for j in range(i + 1, len(kq_nv)):
                if kq_nv[i][1]["nam_sinh"] < kq_nv[j][1]["nam_sinh"]:
                    kq_nv[i], kq_nv[j] = kq_nv[j], kq_nv[i]
        for ma_nv, thong_tin in kq_nv:
            print(f"{ma_nv}:{thong_tin}")
    elif chon == "0":
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")