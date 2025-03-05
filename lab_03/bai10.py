n = int(input("Nhập vào số nguyên dương n: "))  
if n <= 0:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
else:
    print("Phân tích thừa số nguyên tố của", n, "là: ", end="")
    for i in range(2, n + 1):
        for j in range(n):  
            if n % i == 0:
                print(i, end=" ")
                n //= i  
            else:
                break 