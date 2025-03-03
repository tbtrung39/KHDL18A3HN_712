#hình a: 
n = int(input("Nhập số hàng của tam giác là: "))
if n <= 0:
    print("Bạn nhập sai yêu cầu. Vui lòng nhập lại nha")
else:
    k = n - 1
    print("Tam giác (c):")
    for dong in range(1, n + 1):
        for cot in range(k, 0, -1):
            print(" ", end="")
        k = k - 1
        if dong == n:
            khoang_trang = (2 * n - 6) // 2
            for i in range(khoang_trang):
                print(" ", end="")
            for j in range(6):
                print("*", end="")
        else:
           for cot in range(1, dong + 1):
                if cot == 1 or cot == dong:
                    print("*", end=" ") 
                else:
                    print(" ", end=" ")
        print("\r")
#Hình b:
n = int(input("Nhập số hàng của tam giác là: "))
if n <= 0:
    print("Bạn nhập sai yêu cầu. Vui lòng nhập lại nha")
else:
    k = n - 1
    print("Tam giác (c):")
    for dong in range(1, n + 1):
        for cot in range(k, 0, -1):
            print(" ", end="")
        k = k - 1
        for cot in range(1, dong + 1):
            if cot == 1 or cot == dong or dong == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")   
        print("\r")
#c)
n = int(input("Nhập số hàng của tam giác là: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)