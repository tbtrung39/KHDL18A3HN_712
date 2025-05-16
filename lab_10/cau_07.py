import ktradayso

print("=== CHƯƠNG TRÌNH XỬ LÝ DÃY SỐ NGẪU NHIÊN ===")

day_so = ktradayso.sinh_day_so()
print("Dãy số ngẫu nhiên sinh ra:")
print(day_so)

print("\nCác số nguyên tố chia hết cho 7:")
ket_qua_nt = ktradayso.liet_ke_nguyen_to_chia_het_cho_7(day_so)
print(ket_qua_nt if ket_qua_nt else "Không có số nguyên tố chia hết cho 7.")

tong_le = ktradayso.tinh_tong_so_le(day_so)
print(f"\nTổng các số lẻ trong dãy: {tong_le}")

so_cp = ktradayso.kiem_tra_so_chinh_phuong(day_so)
if so_cp:
    print("\nCác số chính phương trong dãy:")
    print(so_cp)
else:
    print("\nKhông có số chính phương trong dãy.")
