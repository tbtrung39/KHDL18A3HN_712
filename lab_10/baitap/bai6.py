from pkg import doicoso2

s = "1010AFG3"
print("Chuỗi sau khi lọc:", doicoso2.loc_ky_tu(s))
print("Chuỗi thuộc hệ cơ số:", doicoso2.co_so_nao(s))

print("Chuyển '1011' từ nhị phân sang thập phân:", doicoso2.bin_to_dec("1011"))
print("Chuyển '17' từ bát phân sang thập phân:", doicoso2.oct_to_dec("17"))
print("Chuyển '1A' từ hex sang thập phân:", doicoso2.hex_to_dec("1A"))