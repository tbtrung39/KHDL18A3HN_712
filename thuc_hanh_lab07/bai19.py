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
    choice = input("Chọn chức năng: ")
    if choice == "1":
        nhan_vien = {} 
        print("Từ điển đã được tạo.")
    elif choice == "2":
        ma_nhan_vien = input("Nhập mã nhân viên (tối đa 4 ký tự): ")
        ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
        nam_sinh = int(input("Nhập năm sinh: "))
        luong = int(input("Nhập lương: "))
        nhan_vien[ma_nhan_vien] = {"Họ tên": ho_ten[:20], "năm sinh": nam_sinh, "lương": luong}
        print("Hoàn thành việc thêm nhân viên.")
    elif choice == "3":
        ma_nhan_vien = input("Nhập mã nhân viên cần tìm: ")
        if ma_nhan_vien in nhan_vien:
            print("Thông tin nhân viên:", nhan_vien[ma_nhan_vien])
        else:
            print("Không tìm thấy nhân viên.")
    elif choice == "4":
        ma_nhan_vien = input("Nhập mã nhân viên cần tăng lương: ")
        if ma_nhan_vien in nhan_vien:
            nhan_vien[ma_nhan_vien]["lương"] += 1000000
            print(f"Đã tăng lương. Lương mới: {nhan_vien[ma_nhan_vien]['lương']}")
        else:
            print("Không tìm thấy nhân viên.")
    elif choice == "5":
        ma_nhan_vien = input("Nhập mã nhân viên cần xóa: ")
        if ma_nhan_vien in nhan_vien:
            moi={}
            for k,v in nhan_vien.items():
                if k != ma_nhan_vien:
                    moi[k]=v
            nhan_vien=moi
            print("Đã xóa nhân viên.")
        else:
            print("Không tìm thấy nhân viên.")
    elif choice == "6":
        kq_nhan_vien = list(nhan_vien.items())
        for i in range(len(kq_nhan_vien)):
            for j in range(i + 1, len(kq_nhan_vien)):
                if kq_nhan_vien[i][1]["nam_sinh"] < kq_nhan_vien[j][1]["nam_sinh"]:
                    kq_nhan_vien[i], kq_nhan_vien[j] = kq_nhan_vien[j], kq_nhan_vien[i]
        for ma_nhan_vien, thong_tin in kq_nhan_vien:
            print(f"{ma_nhan_vien}:{thong_tin}")
    elif choice == "0":
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")