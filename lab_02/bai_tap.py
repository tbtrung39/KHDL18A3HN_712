# Bài 1: Viết chương trình nhập vào thông tin của một sinh viên bao gồm: mã số sinh
# viên, họ tên, quê quán, năm sinh, điểm trung bình các năm học; xuất ra thông
# tin của sinh viên vừa nhập.

# ma_so = input('Nhập mã số sinh viên: ')
# ho_ten = input('Nhập họ tên: ')
# que_quan = input('Nhập quê quán: ')
# nam_sinh = input('Nhập năm sinh: ')
# diem_tb = float(input('Nhập điểm trung bình các năm học: '))
# print('====== Thông tin sinh viên ======')
# print(f'Mã số sinh viên: {ma_so}')
# print(f'Họ tên: {ho_ten}')
# print(f'Quê quán: {que_quan}')
# print(f'Năm sinh: {nam_sinh}')
# print(f'Điểm trung bình các năm học: {diem_tb}')

# Bài 2: Nhập các giá trị s tính bằng giây, m tính bằng phút, h tính bằng giờ, d tính bằng ngày. 
# Viết công thức đổi giá trị “d ngày, h giờ, m phút, s giây”.

# tong_so_giay = int(input('Nhập vào tổng số giây: '))
# d = tong_so_giay // (24 * 3600)
# du = tong_so_giay % (24 * 3600)
# h = du // 3600
# du = du % 3600
# m = du // 60
# s = du % 60
# print(f'{d} ngày, {h} giờ, {m} phút, {s} giây')

# Bài 3: Viết chương trình tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ
# với bán kính và chiều cao nhập từ bàn phím (Làm tròn đến số thập phân thứ hai). Biết
# 𝜋 = pi

# from math import *
# r = float(input('Nhập bán kính: '))
# h = float(input('Nhập chiều cao: '))
# dt_xq = 2 * pi * r * h
# dt_tp = 2 * pi * r * (r + h)
# v = pi * r**2 * h
# print(f'Diện tích xung quanh: {dt_xq:.2f}')
# print(f'Diện tích toàn phần: {dt_tp:.2f}')
# print(f'Thể tích: {v:.2f}')

# Bài 4: 

# from math import *
# x = float(input('Nhập x: '))
# f_x = (-x + sqrt(x**2 + 4)) / ((x**4 + 1)**(1/7))
# print(f'Giá trị của biểu thức: {f_x:.2f}')

# Bài 5:Viết chương trình nhập vào 2 vector a và b. Tính tích vô hướng của 2 vector đó

# a1, a2, a3 = map(float, input('Nhập vector a: ').split())
# b1, b2, b3 = map(float, input('Nhập vector b: ').split())
# tich_vo_huong = a1*b1 + a2*b2 + a3*b3
# print("Tích vô hướng của 2 vector là:", tich_vo_huong)

# Bài 6: Một bóng đèn khi được sử dụng với hiệu điện thế 220 V, có cường độ dòng điện chạy 
# qua bàn là 2,7 A. Viết chương trình nhập vào thời gian sử dụng bóng đèn (giây) tính toán 
# được tiền điện phải trả với giá tiền điện là 7000 đ/kWh.

# t = float(input('Nhập thời gian sử dụng bóng đèn: '))
# u = 220  
# i = 2.7 
# gia_tien = 7000  
# cong_suat = u * i 
# nang_luong_tieu_thu_kwh = (cong_suat * t) / (1000 * 3600) 
# tien_dien = nang_luong_tieu_thu_kwh * gia_tien
# print(f'Tiền điện phải trả: {tien_dien:.2f} đ')

# Bài 7: Viết chương trình nhập vào giá trị a, b, c của một phương trình bậc 2. Tìm đỉnh của
# phương trình bậc 2 đó (Làm tròn đến số thập phân thứ hai).

# a = float(input('Nhập a: '))
# b = float(input('Nhập b: '))
# c = float(input('Nhập c: '))
# x_dinh = -b/(2*a)
# y_dinh = a*x_dinh**2 + b*x_dinh + c
# print(f'Đỉnh của PTB2 là: ({x_dinh:.2f}, {y_dinh:.2f})')

# Bài 8: Viết chương trình nhập vào tọa độ 3 đỉnh A,B,C của một tam giác. Tìm trọng tâm của
# tam giác đó (Làm tròn đến số thập phân thứ hai)

# x_A = float(input('Nhập hoành độ điểm A: '))
# y_A = float(input('Nhập tung độ điểm A: '))
# x_B = float(input('Nhập hoành độ điểm B: '))
# y_B = float(input('Nhập tung độ điểm B: '))
# x_C = float(input('Nhập hoành độ điểm C: '))
# y_C = float(input('Nhập tung độ điểm C: '))
# G_x = (x_A + x_B + x_C) / 3
# G_y = (y_A + y_B + y_C) / 3
# print(f'Tọa độ trọng tâm của tam giác là: ({G_x:.2f}, {G_y:.2f})')

# Bài 9: Viết chương trình nhập vào một tọa độ trong không gian Oxyz. Tính tọa độ của điểm
# đối xứng với nó qua mặt phẳng Oxy, Oxz, Oyz

# x = float(input("Nhập tọa độ x: "))
# y = float(input("Nhập tọa độ y: "))
# z = float(input("Nhập tọa độ z: "))
# dx_Oxy = (x, y, -z)
# dx_Oxz = (x, -y, z)
# dx_Oyz = (-x, y, z)
# print(f"Điểm đối xứng qua mặt phẳng Oxy: {dx_Oxy}")
# print(f"Điểm đối xứng qua mặt phẳng Oxz: {dx_Oxz}")
# print(f"Điểm đối xứng qua mặt phẳng Oyz: {dx_Oyz}")


# Bài 10: Cho biểu thức 𝑓(𝑥) = log4 𝑥 + log𝑥 2
# Viết chương trình nhập vào x và tính giá trị của biểu thức (Làm tròn đến số thập phân thứ hai).

# from math import *
# x = float(input('Nhập x: '))
# f_x = log(x, 4) + log(2, x)
# print(f'Giá trị của biểu thức: {f_x:.2f}')

# Bài 11: Viết chương trình tính xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 (Làm
# tròn đến số thập phân thứ hai)

# n = int(input("Nhập số lần tung xúc sắc: "))
# xac_suat_khong_ra = 1 - (1 / 216)
# xac_suat_it_nhat_mot_lan_ra = 1 - xac_suat_khong_ra**n
# print(f"Xác suất 1 lần cả 3 xúc sắc ra mặt 6 trong {n} lần tung: {xac_suat_it_nhat_mot_lan_ra:.2f}")

# Bài 12: Viết chương trình nhập vào vận tốc a của một xe ô tô đang chạy. Khi người lái đạp
# phanh, tính thời gian ô tô đi được cho đến lúc dừng, biết vận tốc chậm dần đều là 𝑣(𝑡) =
# −𝑡. log4 5 + 𝑎4 (Làm tròn đến số thập phân thứ hai).

# from math import *
# a = float(input('Nhập vận tốc ban đầu của ô tô: '))
# log4_5 = log(5) / log(4)
# t = (a ** 4) / log4_5
# print(f'Thời gian ô tô dừng lại: {t:.2f} giây')
