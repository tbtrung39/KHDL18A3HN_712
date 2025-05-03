def dao_nguoc_so(n, so_dao_nguoc=0):
    if n == 0:
        return so_dao_nguoc
    else:
        so_dao_nguoc = so_dao_nguoc * 10 + n % 1
        return dao_nguoc_so(n // 10, so_dao_nguoc)

n = int(input("Nhập một số: "))
result = dao_nguoc_so(n)
print(f"Số đảo ngược của {n} là: {result}")