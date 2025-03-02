n = int(input("Nhap n: "))

for i in range(1, n+1):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i:
        print(f"{i} là số hoàn hảo")