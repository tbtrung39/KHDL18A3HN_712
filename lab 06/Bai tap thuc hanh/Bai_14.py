password=input("Nhập mật khẩu")
Do_dai=6 <= len(password) <= 12
Chu_viet_thuong=False
Chu_viet_hoa=False
Ky_tu_dac_biet=False
Chu_so=False
special_chars="$#@"
for char in password:
    if "a"  <= char <= "z":
        Chu_viet_thuong=True
    if "0" <= char <= "9":
        Chu_so=True
    if "A" <= char <= "Z":
        Chu_viet_hoa =True
    if char in special_chars:
        Ky_tu_dac_biet=True

if Do_dai and Chu_viet_thuong and Chu_viet_hoa and Ky_tu_dac_biet and Chu_so:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")
    