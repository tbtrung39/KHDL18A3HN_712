n = int(input("Nhập số tự nhiên n: "))
ds = []
so = 2
while len(ds) < n:
    so_nguyen_to = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        ds.append(so)
    so += 1
print("Dãy", n, "số nguyên tố đầu tiên:", ds)