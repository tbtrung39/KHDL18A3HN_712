danh_sach = []
while True:
    du_lieu = input("Nhap tuple (name, age, score) cach nhau boi dau phay (nhap OK de dung): ")
    if du_lieu == "":
        break
    name,age,score = du_lieu.split(",")
    danh_sach.append((name.strip(), int(age.strip()), int(score.strip())))
n = len(danh_sach)
for i in range(n-1):
    for j in range(i+1, n):
        if (danh_sach[i][0] > danh_sach[j][0]) or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] > danh_sach[j][1]) or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] == danh_sach[j][1] and danh_sach[i][2] > danh_sach[j][2]):
            danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
print("\nDanh sach sau khi sap xep:")
for item in danh_sach:
    print(item)