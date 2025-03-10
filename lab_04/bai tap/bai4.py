tu_so = int(input("Nhập tử số: "))

mau_so = 0  # Khởi tạo mẫu số để vào vòng lặp
while mau_so == 0:
    mau_so = int(input("Nhập mẫu số (khác 0): "))
    if mau_so == 0:
        print("Mẫu số không được bằng 0, vui lòng nhập lại.")

print(f"Phân số bạn nhập là: {tu_so}/{mau_so}")
