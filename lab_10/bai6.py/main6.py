import doicoso2

hex_str = input("Nhập số hệ 16: ")
print("Sang thập phân:", doicoso2.hex_to_dec(hex_str))

n = int(input("Nhập số thập phân: "))
print("Sang nhị phân:", doicoso2.dec_to_bin(n))
print("Sang bát phân:", doicoso2.dec_to_oct(n))
print("Sang thập lục phân:", doicoso2.dec_to_hex(n))

bin_str = input("Nhập số nhị phân: ")
print("Sang thập phân:", doicoso2.bin_to_dec(bin_str))

oct_str = input("Nhập số bát phân: ")
print("Sang thập phân:", doicoso2.oct_to_dec(oct_str))