danh_sach = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
 print("Danh sách ban đầu:", danh_sach)
 
 A = set()
 
 print("Nhập 5 số khác nhau từ danh sách trên để đưa vào tập hợp A:")
 
 while len(A) < 5:
     nhap = input("Nhập số thứ " + str(len(A)+1) + ": ")
     if nhap.isdigit():
         so = int(nhap)
         if so in danh_sach and so not in A:
             A.add(so)
         else:
             print("hay nhap mojt so khac voi so da nhap truoc do.")
     else:
         print(" chi nhap 1 chu so.")
 
 print("Tập hợp A gồm 5 phần tử là:", A)