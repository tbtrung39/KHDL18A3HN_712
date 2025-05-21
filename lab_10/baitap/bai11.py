from pkg import doicoso1, doicoso2

n = 42
print("Nhị phân:", doicoso1.to_binary(n))
print("Bát phân:", doicoso1.to_octal(n))
print("Hex:", doicoso1.to_hex(n))

s = "1011AF23Z"
print("Chuỗi sau lọc:", doicoso2.loc_ky_tu(s))
print("Chuỗi thuộc hệ:", doicoso2.co_so_nao(s))
print("Chuyển '1101' từ nhị phân sang thập phân:", doicoso2.bin_to_dec("1101"))