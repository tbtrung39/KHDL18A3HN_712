n = int(input("Nhap so nguyen duong n: "))
if n <= 0:
    print("Vui long nhap lai!")
else:
    S = 0
    for i in range(1, n+1):
        if i % 2 !=0:
            S += i**3
    print(S)