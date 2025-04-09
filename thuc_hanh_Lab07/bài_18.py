dan_sach_thi_sinh={}
while True:
    so_bao_danh=input("Nhập số báo danh :").strip()
    if so_bao_danh=="":
        break
    if so_bao_danh in dan_sach_thi_sinh:
        ho_ten,diem=dan_sach_thi_sinh[so_bao_danh]
        print(f'Thí sinh:{ho_ten},Điểm:{diem}')
    else:
        ho_ten=input("Nhập họ và tên: ").strip()
        diem=float(input("Nhập điểm thi: "))
        dan_sach_thi_sinh[so_bao_danh]=(ho_ten,diem)
        print("Đã thêm thí sinh mới ")