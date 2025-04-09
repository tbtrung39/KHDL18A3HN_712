nhan_vien={}
while True:
    print("\n--- Menu ---\n1. Tạo mới từ điển\n2. Thêm nhân viên\n3. Tìm kiếm nhân viên theo mã\n4. Tăng lương cho nhân viên\n5. Xóa nhân viên\n6. Sắp xếp từ điển theo năm sinh\n7. Thoát")
    chon=int(input("Chọn một chức năng: "))
    if chon==1: nhan_vien={}
    elif chon==2:
        ma_nv=input("Nhập mã nhân viên (4 ký tự): ")
        while ma_nv in nhan_vien:
            print("Mã nhân viên đã tồn tại. Nhập lại.")
            ma_nv=input("Nhập mã nhân viên (4 ký tự): ")
        ho_ten=input("Nhập họ tên (20 ký tự): ")
        nam_sinh=int(input("Nhập năm sinh: "))
        luong=float(input("Nhập lương: "))
        nhan_vien[ma_nv]={'ho_ten':ho_ten,'nam_sinh':nam_sinh,'luong':luong}
    elif chon==3:
        ma_nv=input("Nhập mã nhân viên cần tìm: ")
        if ma_nv in nhan_vien:
            print(f"Mã nhân viên: {ma_nv}, Họ tên: {nhan_vien[ma_nv]['ho_ten']}, Năm sinh: {nhan_vien[ma_nv]['nam_sinh']}, Lương: {nhan_vien[ma_nv]['luong']}")
        else:
            print("Nhân viên không tồn tại.")
    elif chon==4:
        ma_nv=input("Nhập mã nhân viên cần tăng lương: ")
        if ma_nv in nhan_vien:
            nhan_vien[ma_nv]['luong']+=1000000
            print(f"Lương mới của nhân viên {ma_nv} là: {nhan_vien[ma_nv]['luong']}")
        else:
            print("Nhân viên không tồn tại.")
    elif chon==5:
        ma_nv=input("Nhập mã nhân viên cần xóa: ")
        if ma_nv in nhan_vien:
            del nhan_vien[ma_nv]
            print(f"Nhân viên với mã {ma_nv} đã được xóa.")
        else:
            print("Nhân viên không tồn tại.")
    elif chon==6:
        sorted_nv=sorted(nhan_vien.items(),key=lambda x:x[1]['nam_sinh'])
        print("\nDanh sách nhân viên theo năm sinh:")
        for ma_nv,thong_tin in sorted_nv:
            print(f"Mã: {ma_nv}, Họ tên: {thong_tin['ho_ten']}, Năm sinh: {thong_tin['nam_sinh']}, Lương: {thong_tin['luong']}")
    elif chon==7:
        print("Thoát chương trình.")
        break
    else:
        print("Chọn không hợp lệ. Vui lòng thử lại.")
