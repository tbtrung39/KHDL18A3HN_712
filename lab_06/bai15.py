# Nhập danh sách tuple từ bàn phím
danh_sach = []
while True:
    du_lieu = input("Nhập (Tên, Tuổi, Điểm) cách nhau bởi dấu phẩy (bấm Enter để dừng): ")
    if du_lieu == "":
        break
    ten, tuoi, diem = du_lieu.split(",")
    danh_sach.append((ten.strip(), int(tuoi.strip()), int(diem.strip())))
n = len(danh_sach)
for i in range(n - 1):
    for j in range(i + 1, n):
        if (danh_sach[i][0] > danh_sach[j][0]) or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] > danh_sach[j][1]) or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] == danh_sach[j][1] and danh_sach[i][2] > danh_sach[j][2]):
            danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
# In danh sách đã sắp xếp
print("\nDanh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)
