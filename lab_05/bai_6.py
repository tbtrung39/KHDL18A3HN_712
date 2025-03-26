Str = input("Nhap chuoi ky tu Str: ")
he_hex = "0123456789ABCDEF"
hex_hop_le = ""
for char in Str:
    if char in he_hex:
        hex_hop_le += char
if hex_hop_le: 
    n = int(hex_hop_le, 16)
    print(f"Chuoi hop le: {hex_hop_le}")
    print(f"Gia tri thap phan tuong ung: {n}")
else:
    print("Chuoi khong hop le!")