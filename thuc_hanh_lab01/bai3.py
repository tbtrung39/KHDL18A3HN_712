import math

# Nhập bán kính và chiều cao
ban_kinh = float(input("Nhập bán kính: "))
chieu_cao = float(input("Nhập chiều cao: "))

# Tính diện tích xung quanh
dien_tich_xung_quanh = 2 * math.pi * ban_kinh * chieu_cao

# Tính diện tích toàn phần
dien_tich_toan_phan = 2 * math.pi * ban_kinh * (ban_kinh + chieu_cao)

# Tính thể tích
the_tich = math.pi * ban_kinh**2 * chieu_cao

# In kết quả (làm tròn đến 2 chữ số thập phân)
print("Diện tích xung quanh: {:.2f}".format(dien_tich_xung_quanh))
print("Diện tích toàn phần: {:.2f}".format(dien_tich_toan_phan))
print("Thể tích: {:.2f}".format(the_tich))
