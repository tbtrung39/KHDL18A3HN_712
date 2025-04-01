n=int(input("Nhập n: "))
fib=[0,1]
[fib.append(fib[-1]+fib[-2]) for i in range(n-2)]
print(", ".join(map(str,fib[:n])))