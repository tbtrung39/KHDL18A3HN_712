n = int(input("Nhap so n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for i in range(2, n)]
print(", ".join(map(str, fib[:n])))