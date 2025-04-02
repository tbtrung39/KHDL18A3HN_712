ds = []
 while True:
     so = int(input("Nhap danh sach(nhap 0 de dung): "))
     if so == 0:
         break
     ds.append(so)
 print("Danh sach da nhap: ", ds)
 
 ds = [x for x in ds if x > 0] + [x for x in ds if x <= 0]
 print("Danh sách với số dương ở đầu:", ds)
 
 m = int(input("Nhap m: "))
 ds.insert(0, m)
 ds.append(m)
 if len(ds) >= 5:
     ds.insert(4, m)
 else:
     print("Danh sach khong du 5 phan tu, khong the chen vao vi tri thu 5")
 print("Danh sach sau khi chen: ", ds)