x = 100
#phan a
i = 1
n = 1
S = 0
while i<x:
    S += n*1/(i)
    n *= -1
    i += 1
#phan b
S1 = 0
i = 2 
while i<x:
    S1 += n*1/(i*(i-1))
    n *= 1
    i += 1
    
#phan c
S2 = 0
i = 1
while i<x:
    S2 += n*1/(i**0.5)
    n *= 1
    i += 1
    
print(f"kết quả phần a là:{S}")
print(f"kết quả phần b là:{S1}")
print(f"kết quả phần c là:{S2}")