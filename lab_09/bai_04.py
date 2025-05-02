def hoan_vi(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            hoan_vi(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]

n = int(input("Nhap so tu nhien n: "))
if n <= 0:
    print("So tu nhien phai > 0.")
else:
    day = list(range(1, n + 1))
    print(f"Tat ca hoan vi cua day tu 1 -> {n}:")
    hoan_vi(day, 0, n - 1)
