n = int(input("Hay nhap phan tu n=: "))

A = set()
print(f"Nhập {n} số thực (không trùng nhau):")
while len(A) < n:
    du_lieu = input(f"Nhập số thứ {len(A)+1}: ")
    try:
        x = float(du_lieu)
        if x in A:
            print("Hay nhap so khac vif so nay da duoc nhap truoc do")
        else:
            A.add(x)
    except:
        print("Hay nhap so thuc.")
A_list = list(A)             
nho_nhat = A_list[0]         
lon_nhat = A_list[0]         
tong = 0

for x in A_list:
    if x < nho_nhat:
        nho_nhat = x
    if x > lon_nhat:
        lon_nhat = x
    tong += x
print(f"\nTập hợp A: {A}")
print(f"Phần tử nhỏ nhất: {nho_nhat}")
print(f"Phần tử lớn nhất: {lon_nhat}")
print(f"Tổng các phần tử: {tong}")