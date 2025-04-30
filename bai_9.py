def dao_nguoc_so(n, kq=0):
    if n == 0:
        return kq
    return dao_nguoc_so(n // 10, kq * 10 + n % 10)
n = int(input("Nhap so tu ban phim: "))
kq = dao_nguoc_so(n)
print("So dao nguoc la:", kq)
