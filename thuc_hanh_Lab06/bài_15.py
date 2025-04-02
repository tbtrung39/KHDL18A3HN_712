danh_sach_tuple = []
while True:
    dau_vao = input("Nhập tuple (name age score) hoặc 'done' để kết thúc: ")
    if dau_vao.lower() == 'done':
        break
    try:
        name, age, score = dau_vao.split()
        danh_sach_tuple.append((name, int(age), int(score)))  
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập đúng định dạng.")
danh_sach_tuple_sap_xep = sorted(danh_sach_tuple, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách tuple sau khi sắp xếp:")
for tuple_item in danh_sach_tuple_sap_xep:
    print(tuple_item)