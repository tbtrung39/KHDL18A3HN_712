s=input("nhap chuoi: ").upper()
ds_hex="0123456789ABCDEF"
hop_le=""
for c in s:
    if c in ds_hex:
        hop_le+=c
if hop_le:
    n=int(hop_le, 16)
    print("chuoi hop le la:", hop_le)
    print("gia tri thap phan:", n)
else:
    print("chuoi khong co ki tu hop le")