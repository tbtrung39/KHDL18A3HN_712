# #cau1
# import my_Triange
# print("=== KIỂM TRA TAM GIÁC ===")
# a = float(input("Nhập cạnh a: "))
# b = float(input("Nhập cạnh b: "))
# c = float(input("Nhập cạnh c: "))
# chu_vi = my_Triange.chu_vi_tam_giac(a, b, c)
# dien_tich = my_Triange.dien_tich_tam_giac(a, b, c)
# if chu_vi is not None and dien_tich is not None:
#     print(f"Chu vi tam giác: {chu_vi}")
#     print(f"Diện tích tam giác: {dien_tich}")
#     kiem_tra = my_Triange.check_tam_giac(a, b, c)
#     print(f"==> Ba số {a}, {b}, {c} có tạo thanh một tam giác không?")
#     print("True" if kiem_tra else "False")
# else:
#     print("Cạnh tam giác phải là số dương.")

# #cau2
# import my_square
# print("=== TÍNH TOÁN HÌNH VUÔNG ===")
# a = float(input("Nhập độ dài cạnh hình vuông: "))
# chu_vi = my_square.chu_vi_hinh_vuong(a)
# dien_tich = my_square.dien_tich_hinh_vuong(a)
# if chu_vi is not None and dien_tich is not None:
#     print(f"Chu vi hình vuông: {chu_vi}")
#     print(f"Diện tích hình vuông: {dien_tich}")
# else:
#     print("Cạnh hình vuông phải lớn hơn 0.")


# #cau3
# import sohoc
# print("=== CHƯƠNG TRÌNH SỐ HỌC ===")
# a = int(input("Nhập số nguyên a: "))
# b = int(input("Nhập số nguyên b: "))
# n = int(input("Nhập số nguyên n: "))

# print(f"→ Ước chung lớn nhất của {a} và {b}: {sohoc.Ucln(a, b)}")
# print(f"→ Bội chung nhỏ nhất của {a} và {b}: {sohoc.Bcnn(a, b)}")
# print(f"→ Tổng các ước của {n}: {sohoc.SumDivisor(n)}")



# #cau4
# import giai_pt
# print("1. Giải phương trình bậc nhất.")
# print("2. Giải phương trình bậc hai.")
# lua_chon = input("Nhập lựa chọn (1 hoặc 2): ")

# if lua_chon == "1":
#     a = float(input("Nhập a: "))
#     b = float(input("Nhập b: "))
#     ket_qua = giai_pt.giai_pt_bac_nhat(a, b)
#     print("Kết quả:", ket_qua)
# elif lua_chon == "2":
#     a = float(input("Nhập a: "))
#     b = float(input("Nhập b: "))
#     c = float(input("Nhập c: "))
#     ket_qua = giai_pt.giai_pt_bac_hai(a, b, c)
#     print("Kết quả:", ket_qua)
# else:
#     print("Lựa chọn không hợp lệ.")


# #cau5
# import doicoso1
# so = doicoso1.nhap_so_nguyen()

# print(f"Số vừa nhập: {so}")
# print(f"Số ở hệ nhị phân (base 2): {doicoso1.doi_nhi_phan(so)}")
# print(f"Số ở hệ bát phân (base 8): {doicoso1.doi_bat_phan(so)}")
# print(f"Số ở hệ thập lục phân (base 16): {doicoso1.doi_thap_luc_phan(so)}")


# #cau6
# import doicoso2

# chuoi_nhap = input("Nhập chuỗi số: ")
# chuoi_sau_loai = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi_nhap)
# print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", chuoi_sau_loai)
# co_so = doicoso2.kiem_tra_co_so(chuoi_sau_loai)
# print(f"Cơ số của chuỗi này là: {co_so}")
# if co_so == 2:
#     print("Chuyển từ cơ số 2 sang cơ số 10:", doicoso2.chuyen_2_sang_10(chuoi_sau_loai))
# elif co_so == 8:
#     print("Chuyển từ cơ số 8 sang cơ số 10:", doicoso2.chuyen_8_sang_10(chuoi_sau_loai))
# elif co_so == 16:
#     print("Chuyển từ cơ số 16 sang cơ số 10:", doicoso2.chuyen_16_sang_10(chuoi_sau_loai))
# else:
#     print("Chuyển từ cơ số 10 sang cơ số 10:", chuoi_sau_loai)


# #cau7
# import dayso
# day_so = dayso.sinh_day_so()
# print("Dãy số ngẫu nhiên sinh ra:")
# print(day_so)

# print("\nCác số nguyên tố chia hết cho 7:")
# ket_qua_nt = dayso.liet_ke_nguyen_to_chia_het_cho_7(day_so)
# print(ket_qua_nt if ket_qua_nt else "Không có số nguyên tố chia hết cho 7.")

# tong_le = dayso.tinh_tong_so_le(day_so)
# print(f"\nTổng các số lẻ trong dãy: {tong_le}")

# so_cp = dayso.kiem_tra_so_chinh_phuong(day_so)
# if so_cp:
#     print("\nCác số chính phương trong dãy:")
#     print(so_cp)
# else:
#     print("\nKhông có số chính phương trong dãy.")



# #cau8
# import Matranvuong
# N = int(input("Nhập kích thước ma trận N (NxN): "))
# ma_tran = Matranvuong.nhap_ma_tran(N)
# print("\nMa trận đã nhập:")
# Matranvuong.in_ma_tran(ma_tran)
# ma_tran_chuyen_vi = Matranvuong.ma_tran_chuyen_vi(ma_tran)
# print("\nMa trận chuyển vị:")
# Matranvuong.in_ma_tran(ma_tran_chuyen_vi)

# doi_xung = Matranvuong.kiem_tra_doi_xung(ma_tran)
# print("\n==> Ma trận có đối xứng không?")
# print("True" if doi_xung else "False")


# #cau9
# import qly
# danh_sach = qly.nhap_mat_hang()
# qly.tinh_thanh_tien_va_thue(danh_sach)
# qly.in_danh_sach(danh_sach)
# danh_sach_sx = qly.sap_xep_giam_theo_thue(danh_sach)
# print("\n--- DANH SÁCH SAU KHI SẮP XẾP GIẢM DẦN THEO THUẾ ---")
# qly.in_danh_sach(danh_sach_sx)
  

#cau10
