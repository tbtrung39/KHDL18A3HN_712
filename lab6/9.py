# bai 9
danh_sach = []
while True:
    try:
        so = int(input("Nhập một số (nhập 'done' để kết thúc): "))
        danh_sach.append(so)
    except ValueError:
        break

for so in danh_sach:
    assert so % 2 == 0, f"Số {so} không phải là số chẵn."

print("Tất cả các số trong danh sách đều là số chẵn.")