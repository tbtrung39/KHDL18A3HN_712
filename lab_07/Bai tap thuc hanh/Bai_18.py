sinh_vien={}
n=int(input("Nhập số lượng sinh viên:"))
for i in range(n):
    ma_sv=input("Nhập mã số sinh viên:")
    ten=input("Nhập họ  và tên:")
    diem=float(input("Nhập điểm thi:"))
    sinh_vien[ma_sv]={"Họ và tên":ten,"Điểm":diem}
ma_sv=input("Nhập số báo danh để tra cứu:")
print(sinh_vien.get(ma_sv,"Không tìm thấy sinh viên"))