n=int(input("nhập số n: "))
fibo=[0,1]
[fibo.append(fibo[-1]+fibo[-2]) for i in range(2,n+1)]
print(", ".join(map(str,fibo)))