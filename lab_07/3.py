A = set()
while True:
    n = int(input("Nhap n: "))
    if n == 234:
        break
    else:
        A.add(n)
print(A)
print(min(A))
print(max(A))
print(sum(A))