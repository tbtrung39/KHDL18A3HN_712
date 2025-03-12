tu=int(input("nhập vào tử số: "))
while True:
    mau=int(input("nhập vào mẫu số: "))
    if mau==0:
        print("mẫu số không thể bằng 0, vui lòng nhập lại")
    else:
        print(f"phân số: {tu}/{mau}")
