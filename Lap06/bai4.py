ds = []
 while True:
     so = int(input("Nhap danh sach so tu nhien(nhap 0 de dung): "))
     if so == 0:
         break
     elif so < 0:
         print("Vui long nhap so tu nhien >= 0")
         continue
     ds.append(so)
 print("Danh sach da nhap: ", ds)
 
 ds_chen = [1,2,3]
 ds[0:0] = ds_chen
 ds.extend(ds_chen)
 if len(ds) > 4:
     ds[4:4] = ds_chen
 else:
     print("Danh sach khong du 5 phan tu de chen")
 print("Danh sach sau khi chen: ", ds)
 
 
 if len(ds) > 0:  
     k = int(input("Nhap vi tri can xoa: ".format(len(ds)-1)))
     if 0 <= k < len(ds):
         ds.pop(k)
         print("Danh sach sau khi xoa phan tu: ".format(k), ds)
     else:
         print("Vi tri khong hop le!")
 else:
     print("Danh sach rong, khong the xoa!")
 
 ds.sort()
 print("Danh sach sap xep tang dan: ", ds)
 
 
 ds.sort(reverse=True)
 print("Danh sach sap xep giam dan: ", ds)