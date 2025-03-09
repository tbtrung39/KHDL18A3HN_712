tu = int(input("Nhập tử số của phân số đó: "))
mau = int(input("Nhập mẫu số của phân số đó: "))
while True:
    if mau != 0:
        break
    else:
        print("Vui lòng nhập lại mẫu số ")
phan_so = tu/mau
print(f"Phân số là: {tu}/{mau} = {phan_so}")