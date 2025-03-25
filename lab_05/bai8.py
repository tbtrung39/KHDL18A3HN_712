# cach 1
doan_van = input("Hay nhap doan van: ")
tu_don = input("Hay nhap tu don: ")
# tach doan van va nhap thanh danh sach
tu_don_t = doan_van.split()
count = 0
for i in tu_don_t:
    if i == tu_don:
        count += 1
print("so lan xuat hien cua tu",tu_don,"trong doan van la: ",count)
# cach 2
doan_van=input("Hay nhap doan van: ")
tu_don=input("Hay nhap tu don: ")
# tach cac tu trong van ban
doan_van_t = ""
count=0
for char in doan_van:
    if char.isalpha():
        doan_van_t += char
    else:
        if doan_van_t != "":
            if doan_van_t == tu_don:
                count += 1
            doan_van_t = ""
if doan_van_t == tu_don:
    count += 1 # kiem tra lai
print("tu don",tu_don,"'xuat hien",count,"lan trong doan van da nhap ")