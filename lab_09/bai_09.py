def dao_nguoc(n, so_dao_nguoc=0):
    if n == 0:
        return so_dao_nguoc
    else:
        so_dao_nguoc = so_dao_nguoc * 10 + n % 1
        return dao_nguoc(n // 10, so_dao_nguoc)

n = int(input("Nhap so: "))
kq = dao_nguoc(n)
print(f"So dao nguoc cua {n} la: {kq}")