print("Nhập tử số và mẫu số của môt phân số:")
tu_so=int(input("Nhập tử số:"))
mau_so=0
while mau_so == 0:
    mau_so=int(input("Nhập mẫu số:"))
    if mau_so == 0:
        print("Mẫu số không dược bằng 0")

print(f"Phân số bạn vừa nhập là:{tu_so}/{mau_so}")