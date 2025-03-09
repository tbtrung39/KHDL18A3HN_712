tu_so = int(input("Nhap tu so: "))
mau_so = int(input("Nhap mau so: "))
while mau_so == 0:
    print("Mau so khong the bang 0")
    mau_so = int(input("Nhap mau so: "))
print(f"Phan so da nhap: {tu_so}/{mau_so}")