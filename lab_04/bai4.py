tu_so=int(input('Nhập tử số của phân số: '))
while True:
    mau_so=int(input('Nhập mẫu số của phân số: '))
    if mau_so==0:
        print("Vui lòng nhập mẫu số khác 0")
    else:
        break
print(f"Phân số vừa nhập là: {tu_so}/{mau_so}")