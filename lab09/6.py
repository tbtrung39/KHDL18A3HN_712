def hoan_vi(arr, trai, phai):
    if trai == phai:
        print(arr)
    else:
        for i in range(trai, phai + 1):
            arr[trai], arr[i] = arr[i], arr[trai]
            hoan_vi(arr, trai + 1, phai)
            arr[trai], arr[i] = arr[i], arr[trai]
n = 3
day = [i for i in range(1, n + 1)]
hoan_vi(day, 0, n - 1)
