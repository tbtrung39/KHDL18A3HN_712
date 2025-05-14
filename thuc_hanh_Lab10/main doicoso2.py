import doicoso2
s = input("Nhập chuỗi ký tự bất kỳ: ")
hop_le = doicoso2.loc_ky_tu_hop_le(s)
print("Chuỗi sau khi lọc ký tự hợp lệ (0-9, A-F):", hop_le)
co_so = doicoso2.xac_dinh_co_so(hop_le)
print(f"Chuỗi có thể biểu diễn từ hệ cơ số {co_so} trở lên.")
print("\n=> Đổi từ hệ 2:", doicoso2.chuyen_sang_thap_phan(hop_le, 2))
# Đổi từ hệ 8
print("=> Đổi từ hệ 8:", doicoso2.chuyen_sang_thap_phan(hop_le, 8))
# Đổi từ hệ 16
print("=> Đổi từ hệ 16:", doicoso2.chuyen_sang_thap_phan(hop_le, 16))
