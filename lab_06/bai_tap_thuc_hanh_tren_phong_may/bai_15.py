danh_sach_tuple = []
while True:
    nhap_lieu = input("Nhập tuple (name, age, score) hoặc 'done' để kết thúc: ")
    if nhap_lieu.lower() == 'done':
        break
    try:
        name, age, score = nhap_lieu.split(',')
        age, score = int(age.strip()), int(score.strip())
        danh_sach_tuple.append((name.strip(), age, score))
    except ValueError:
        print("Định dạng nhập không hợp lệ. Vui lòng nhập lại.")
danh_sach_tuple.sort(key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách tuple sau khi sắp xếp:")
for tuple_item in danh_sach_tuple:
    print(tuple_item)