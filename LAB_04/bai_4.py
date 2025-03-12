tu = int(input("nhập tử số:"))
mau = int(input("nhập mẫu số:"))
while mau == 0:
    print("không hợp lệ vui lòng nhập lại")
    mau = int(input("nhập mẫu số:"))
    break
print(f"phân số là {tu}/{mau}")