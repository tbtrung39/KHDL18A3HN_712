class SinhVien:
    def thong_tin_sinh_vien(self, ma_sv, ho_ten, que_quan, nam_sinh, diem_tb):
        self.ma_sinh_vien = ma_sinh_vien
        self.ho_ten = ho_ten
        self.que_quan = que_quan
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb
ma_sinh_vien = int(input("Nhập thông tin của mã sinh viên: "))
ho_ten = input("Nhập họ và tên của sinh viên là: ")
que_quan =input("Nhập thông tin nơi ở của sinh viên là: ")
nam_sinh = int(input("Nhập năm sinh cua sinh viên là: "))
diem_tb = float(input("Nhập điểm trung bình các năm học của sinh viên: "))
sinh_vien = SinhVien()
sinh_vien = SinhVien(ma_sinh_vien,ho_ten,que_quan,nam_sinh,diem_tb)
print("\nThông tin sinh viên vừa nhập:")
print(f'Mã sinh viên: {sinh_vien.ma_sinh_vien}')
print(f'Họ tên: {sinh_vien.ho_ten}')
print(f'Quê quán: {sinh_vien.que_quan}')
print(f'Năm sinh: {sinh_vien.nam_sinh}')
print(f'Điểm trung bình: {sinh_vien.diem_tb}')