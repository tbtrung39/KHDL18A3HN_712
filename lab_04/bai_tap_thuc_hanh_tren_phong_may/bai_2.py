import math

while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

# Tính tổng a
S_a = 0
i = 1
while i <= n:
    if i % 2 == 1:  
        S_a += 1 / i
    else:           
        S_a -= 1 / i
    i += 1
print("Tổng S_a =", S_a)
# Tính tổng b
S_b = 0
i = 2
while i <= n:
    S_b += 1 / (i * (i + 1))
    i += 1
print("Tổng S_b =", S_b)
# Tính tổng c
S_c = 0
i = 2
while i <= n:
    S_c += 1 / math.sqrt(i)
    i += 1
print("Tổng S_c =", S_c)
