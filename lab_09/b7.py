# bai 7
def bo_nghiem(N, n, x=[], tong=0):
    if len(x) == n:
        if tong == N:
            print(x)
        return
    for i in range(N - tong + 1):
        bo_nghiem(N, n, x + [i], tong + i)
N = int(input("Nhap so tu nhien N: "))
n = int(input("Nhap so tu nhien n: "))
bo_nghiem(N, n)
