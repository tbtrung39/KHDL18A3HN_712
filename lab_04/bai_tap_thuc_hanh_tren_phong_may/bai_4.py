tu_so = int(input("Nhập tử số: "))

mau_so = int(input("Nhập mẫu số: "))
while mau_so == 0:
    print("Mẫu số không thể bằng 0, vui lòng nhập lại!")
    mau_so = int(input("Nhập mẫu số: "))

print(f"Phân số bạn đã nhập là: {tu_so}/{mau_so}")
