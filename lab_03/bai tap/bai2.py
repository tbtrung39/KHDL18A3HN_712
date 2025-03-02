n = int(input("Nhập n: "))
so_hoan_hao = []
for i in range(2, n):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i:
        so_hoan_hao.append(i)
print("Các số hoàn hảo nhỏ hơn n:", so_hoan_hao)