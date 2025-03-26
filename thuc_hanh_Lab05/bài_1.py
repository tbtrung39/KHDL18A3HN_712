Str = input("Nhập chuỗi: ")
S = 0
chu_cai = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
for ky_tu in Str:
    if ky_tu not in chu_cai and ky_tu not in chu_so:
        S += 1
print("Số ký tự không phải chữ và số:", S)
