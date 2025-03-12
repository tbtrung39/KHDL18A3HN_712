tu_so = int(input("Nhập tử số: "))
while True:
    mau_so = int(input("Nhập mẫu số (khác 0): "))
    if mau_so != 0:
        break
    print("Mẫu số không thể bằng 0, vui lòng nhập lại!")
print(f"Phân số bạn đã nhập: {tu_so}/{mau_so}")