danh_sach = []
print("Nhập các số tự nhiên (nhập xong bấm Enter để dừng):")
while True:
    nhap = input()
    if nhap == "":
        break
    try:
        so = int(nhap)
        danh_sach.append(so)
    except:
        print("Vui lòng nhập số tự nhiên!")
for so in danh_sach:
    assert so % 2 == 0, f"Số {so} không phải số chẵn!"

print("Tất cả số trong danh sách đều là số chẵn.")