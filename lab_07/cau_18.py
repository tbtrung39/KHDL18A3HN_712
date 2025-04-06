thi_sinh_dict = {}
while True:
    so_bao_danh = input("Nhập số báo danh: ")
    if so_bao_danh in thi_sinh_dict:
        ho_ten, diem = thi_sinh_dict[so_bao_danh]
        print(f"Họ và tên: {ho_ten}, Điểm thi: {diem}")
    else:
        ho_ten = input("Nhập họ và tên thí sinh: ")
        diem = float(input("Nhập điểm thi thí sinh (0-10): "))
        if 0 <= diem <= 10:
            thi_sinh_dict[so_bao_danh] = (ho_ten, diem)
            print(f"Đã thêm thông tin thí sinh: {ho_ten}, Điểm thi: {diem}")
        else:
            print("Điểm thi không hợp lệ, phải nằm trong khoảng từ 0 đến 10.")
    tiep_tuc = input("Bạn có muốn nhập thêm không? (y/n): ").lower()
    if tiep_tuc != 'y':
        break
