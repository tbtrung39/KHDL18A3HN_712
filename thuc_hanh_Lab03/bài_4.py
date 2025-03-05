n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:")
for so in range(2, n + 1): 
    nguyên_tố = 1  
    for i in range(2, (so // 2) + 1):  
        if so % i == 0:
            nguyên_tố = 0 
            break
    if nguyên_tố == 1:  
        print(so, end=" ")
