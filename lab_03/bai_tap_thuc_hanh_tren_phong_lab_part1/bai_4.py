n = int(input("Nhập n: "))
for i in range(2, n + 1):  
    kiem_tra_so_nguyen_to = True
    for j in range(2, int(i**0.5) + 1):  
        if i % j == 0:
            kiem_tra_so_nguyen_to = False
            break
    if kiem_tra_so_nguyen_to:
        print(i, end=" ")  
