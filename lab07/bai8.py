A = set()
print("Nhap cac phan tu cho tap A=.")
print("Nhap 'xong' de ket thuc.")

while True:
    du_lieu = input("Hay nhap phan tu: ")
    if du_lieu == "xong":
        break

    if du_lieu.isdigit():
        A.add(int(du_lieu))  
    elif du_lieu.replace(".", "", 1).isdigit() and du_lieu.count(".") == 1:
        A.add(float(du_lieu))
    else:
        A.add(du_lieu)  
so_nguyen = 0
so_thuc = 0
chuoi = 0

for ptu in A:
    if type(ptu) == int:
        so_nguyen += 1
    elif type(ptu) == float:
        so_thuc += 1
    elif type(ptu) == str:
        chuoi += 1
print("Tập hợp A là:", A)
print("Số phần tử là số nguyên:", so_nguyen)
print("Số phần tử là số thực:", so_thuc)
print("Số phần tử là chuỗi ký tự:", chuoi)