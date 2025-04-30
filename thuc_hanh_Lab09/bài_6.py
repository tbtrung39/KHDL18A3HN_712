def tim_nghiem(n, tong, day=[]):
    if n == 0:
        if tong == 0:
            print(day)
        return
    for i in range(tong + 1):
        tim_nghiem(n - 1, tong - i, day + [i])
n = int(input("Nhập số lượng biến n: "))
N = int(input("Nhập tổng N: "))
tim_nghiem(n, N)
