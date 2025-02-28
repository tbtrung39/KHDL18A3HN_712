so = int(input("Nhập vào một số nguyên dương: "))
if so < 2:
    print("Số nhập vào không hợp lệ")
else:
    for i in range(2, so + 1):
        if so % i == 0:
            print(i, end=" ")
            so = so // i
            if so % i == 0:
                print(i, end=" ")
                so = so // i
            if so % i == 0:
                print(i, end=" ")
                so = so // i