sinh_vien = {}
 n = int(input("Nhập số lượng sinh viên: "))
 i = 0
 while i < n:
     print("\nNhập thông tin sinh viên thứ", i + 1)
     ma = input("Mã sinh viên (6 chữ số): ")
     while len(ma) != 6 or not ma.isdigit():
         print("Mã không hợp lệ! Mời nhập lại.")
         ma = input("Mã sinh viên (6 chữ số): ")
     ten = input("Tên sinh viên: ")
     diem = float(input("Điểm (có thể là số thực): "))
     diem = round(diem)
     if diem < 0:
         diem = 0
     if diem > 10:
         diem = 100
     sinh_vien[ma] = (ten, diem)
     i += 1
 
 danh_sach_sap_xep = sorted(sinh_vien.items(), key=lambda x: x[1][1], reverse=True)
 
 print("\nDanh sách sinh viên sắp xếp theo điểm giảm dần:")
 for ma, (ten, diem) in danh_sach_sap_xep:
     print("Mã:", ma, "| Tên:", ten, "| Điểm:", diem)