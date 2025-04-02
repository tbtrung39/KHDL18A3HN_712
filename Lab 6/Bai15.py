#Bai15
print("Nhập danh sách tuple (name, age, score), nhập 0 để kết thúc:")
lst = []
while True:
    nhap_du_lieu = input("Nhập (name, age, score): ")
    if nhap_du_lieu.lower() == '0':
        break
    du_lieu_tach = nhap_du_lieu.split(",")
    if len(du_lieu_tach) == 3:
        name, age, score = du_lieu_tach
        if age.strip().isdigit() and score.strip().isdigit():
            lst.append((name.strip(), int(age.strip()), int(score.strip())))
        else:
            print("Nhập sai, vui lòng nhập lại!")
    else:
        print("Không hợp lệ, vui lòng nhập lại theo dạng: name, age, score")
danh_sach_sap_xep = sorted(lst, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách sau khi sắp xếp:")
for i in danh_sach_sap_xep:
    print(i)