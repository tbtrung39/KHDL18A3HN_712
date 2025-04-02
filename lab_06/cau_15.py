danh_sach = []
print("Nhập danh sách (tên, tuổi, điểm), nhập 'done' để kết thúc:")
while True:
    du_lieu = input("Nhập (tên, tuổi, điểm): ")
    if du_lieu.lower() == "done":
        break
    phan_tu = du_lieu.split(",")
    if len(phan_tu) == 3 and phan_tu[1].strip().isdigit() and phan_tu[2].strip().isdigit():
        ten, tuoi, diem = phan_tu
        danh_sach.append((ten.strip(), int(tuoi.strip()), int(diem.strip())))
    else:
        print("Dữ liệu không hợp lệ! Vui lòng nhập theo format: tên, tuổi, điểm")
danh_sach_sap_xep = sorted(danh_sach, key=lambda x: (x[0], -x[1], -x[2]))
print("\nDanh sách sau khi sắp xếp:")
for muc in danh_sach_sap_xep:
    print(muc)