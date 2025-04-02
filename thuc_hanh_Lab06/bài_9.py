danh_sach_nhap = []
while True:
    so_nhap = input("Nhập một số (nhập 'done' để kết thúc): ")
    if so_nhap.lower() == 'done':
        break
    try:
        danh_sach_nhap.append(int(so_nhap))
    except ValueError:
        print("Vui lòng nhập một số hoặc 'done'.")
for so in danh_sach_nhap:
    assert so % 2 == 0, f"Số {so} không phải là số chẵn."

print("Tất cả các số trong danh sách đều là số chẵn.")