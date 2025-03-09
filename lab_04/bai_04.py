tu = int(input("nhập tử số: "))
mau = int(input("nhập mẫu số: "))
while mau == 0:
    print("mẫu số không thể bằng 0")
    mau = int(input("hãy nhập lại mẫu số: "))
print("phân số hợp lệ:", tu, "/", mau)