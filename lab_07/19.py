nv_dict = {}

def tao_moi():
    global nv_dict
    nv_dict = {}
    print("Đã tạo mới từ điển.")

def them_nv():
    ma = input("Nhập mã nhân viên (4 ký tự): ")
    ten = input("Nhập họ tên: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    luong = int(input("Nhập lương: "))
    nv_dict[ma] = [ten, nam_sinh, luong]

def tim_nv():
    ma = input("Nhập mã nhân viên cần tìm: ")
    if ma in nv_dict:
        print(f"Họ tên: {nv_dict[ma][0]}, Năm sinh: {nv_dict[ma][1]}, Lương: {nv_dict[ma][2]}")
    else:
        print("Không tìm thấy.")

def tang_luong():
    for ma in nv_dict:
        nv_dict[ma][2] += 100000
    print("Đã tăng lương cho tất cả nhân viên.")

def xoa_nv():
    ma = input("Nhập mã nhân viên cần xóa: ")
    if ma in nv_dict:
        del nv_dict[ma]
        print("Đã xóa.")
    else:
        print("Không tìm thấy.")

def sap_xep():
    sap_xep_ds = sorted(nv_dict.items(), key=lambda x: x[1][1], reverse=True)
    print("Danh sách nhân viên theo năm sinh giảm dần:")
    for ma, tt in sap_xep_ds:
        print(f"{ma} - {tt[0]}, {tt[1]}, Lương: {tt[2]}")

while True:
    print("\n--- MENU ---")
    print("1. Tạo mới từ điển")
    print("2. Thêm nhân viên")
    print("3. Tìm kiếm nhân viên")
    print("4. Tăng lương")
    print("5. Xóa nhân viên")
    print("6. Sắp xếp theo năm sinh")
    print("0. Thoát")

    chon = input("Chọn thao tác: ")
    if chon == "1": tao_moi()
    elif chon == "2": them_nv()
    elif chon == "3": tim_nv()
    elif chon == "4": tang_luong()
    elif chon == "5": xoa_nv()
    elif chon == "6": sap_xep()
    elif chon == "0": break
    else: print("Lựa chọn không hợp lệ.")
