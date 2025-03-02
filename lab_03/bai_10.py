while True:
    n = int(input("Nhap n nguyen duong: "))
    if n > 0:
        break
    print("n phai la so nguyen duong. Vui long nhap lai!")

print(f"{n} = ", end="")
i = 2
first = True

while n > 1:
    count = 0
    while n % i == 0:
        count += 1
        n //= i
    if count > 0:
        if first:
            first = False
        else:
            print(" x ", end="")
        if count == 1:
            print(i, end="")
        else:
            print(f"{i}^{count}", end="")
    i += 1