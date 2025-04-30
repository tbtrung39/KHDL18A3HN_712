def ham_dao_nguoc(n, rev=0):
    if n == 0:
        return rev
    else:
        return ham_dao_nguoc(n // 10, rev * 10 + n % 10)

x = int(input("Nhập số cần đảo ngược: "))
print("Số sau khi đảo ngược là:", ham_dao_nguoc(x))
