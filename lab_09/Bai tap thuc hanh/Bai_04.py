def hoan_vi(arr, vitri=0):
    if vitri == len(arr):
        print(arr)
    else:
        for i in range(vitri, len(arr)):
            arr[vitri], arr[i] = arr[i], arr[vitri]
            hoan_vi(arr, vitri + 1)
            arr[vitri], arr[i] = arr[i], arr[vitri]

n = int(input("Nhập một số tự nhiên n: "))
arr = list(range(1, n + 1))
hoan_vi(arr)
