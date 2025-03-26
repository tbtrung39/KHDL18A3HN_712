Str = input("Nhap chuoi: ")
hex = ""
for i in Str:
    if i in "0123456789ABCDEFabcdef":
        hex += i
if hex:
    he_10 = int(hex, 16)
    print(f"Chuoi hop le trong he Hex: {hex}")
    print(f"Khi chuyen sang he 10: {he_10}")
else:
    print("Chuoi khong chua ky tu hop le!!!")