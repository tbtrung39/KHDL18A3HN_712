while True:
    so_n = int(input("Nhap n nguyen duong: "))
    if so_n > 0:
        break
    print("n phai la so nguyen duong. Vui long nhap lai!")

print(f"{so_n} = ", end="")
so_dau = True

for i in range(2, so_n + 1):
    so_mu = 0
    while so_n % i == 0:
        so_mu += 1
        so_n //= i
    
    if so_mu > 0:
        if not so_dau:
            print(" x ", end="")
        if so_mu == 1:
            print(i, end="")
        else:
            print(f"{i}^{so_mu}", end="")
        so_dau = False
    
    if so_n == 1:
        break