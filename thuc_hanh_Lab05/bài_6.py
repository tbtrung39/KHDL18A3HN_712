chuoi = input("Nhập chuỗi: ")
chuoi_hex = "0123456789ABCDEFabcdef"
hex_hop_le = ""
for ky_tu in chuoi:
    if ky_tu in chuoi_hex:
        hex_hop_le += ky_tu
print("Chuỗi Hex hợp lệ sau khi lọc:", hex_hop_le)
if hex_hop_le:
    so_thap_phan = int(hex_hop_le, 16)
    print("Giá trị thập phân tương ứng:", so_thap_phan)
else:
    print("Không có số hợp lệ để chuyển đổi.")
