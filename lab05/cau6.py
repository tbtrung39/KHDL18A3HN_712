s=input("nhập chuỗi: ").upper()
ds_hex="0123456789ABCDEF"
hop_le=""
for c in s:
    if c in ds_hex:
        hop_le+=c
if hop_le:
    n=int(hop_le, 16)
    print("chuỗi hợp lệ là:", hop_le)
    print("giá trị thập phân:", n)
else:
    print("chuỗi không có kí tự hợp lệ trong hệ hex.")

