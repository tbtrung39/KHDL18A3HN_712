def hoan_vi(day, l, r):
    if l == r:
        print(day)
    else:
        for i in range(l, r + 1):
            day[l], day[i] = day[i], day[l]
            hoan_vi(day, l + 1, r)
            day[l], day[i] = day[i], day[l]  
n = int(input("Nhập n: "))
day_so = list(range(1, n + 1))
hoan_vi(day_so, 0, n - 1)
