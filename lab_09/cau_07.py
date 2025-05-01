def tim_bo_nhiem(N, n, bo_nhiem=[], index = 0):
    if index == n:
        if sum(bo_nhiem) == N:
            print(bo_nhiem)
        return
    for i in range(N + 1):
        tim_bo_nhiem(N, n, bo_nhiem + [i], index + 1)

N = int(input("Nhập số N: "))
n = int(input("Nhập số tự nhiên n: "))
tim_bo_nhiem(N, n)

