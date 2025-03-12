import os
print("/n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.")
while True:
    print("Menu chọn thức ăn")
    print("1.Cafe")
    print("2.Cam vắt")
    print("3.Nước ép cà rốt")
    print("4.Nước lọc")
    print("5.Nước dừa")
    n = int(input("nhập số từ 1-4:"))
    if n == 1:
        print("bạn chọn cafe")
    elif n == 2:
        print("bạn chọn cam vắt")
    elif n == 3:
        print("bạn chọn nước ép cà rốt")
    elif n == 4:
        print("bạn chọn nước lọc")
    elif n == 5:
        print("bạn chọn nước dừa")
    else:
        print("vui lòng nhập lại")
        break
    t = int(input("nhập 0 muốn thoát"))
    if t == 0:
        break
    else:os.system('cls')
    