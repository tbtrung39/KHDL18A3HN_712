def dao_nguoc_so(n, dao_nguoc=0):
    if n == 0:
        return dao_nguoc
    else:
        return dao_nguoc_so(n // 10, dao_nguoc * 10 + n % 10)
    
n = int(input("Nhập số: "))
print("Số đảo ngược là:", dao_nguoc_so(n))
