n = int(input("Nhập n: "))
print(f"Các số hoàn hảo nhỏ hơn {n} là:")
for i in range(2, n):  
    S = 0
    for j in range(1, i):  
        if i % j == 0:
            S += j
    if S == i: 
        print(i)
