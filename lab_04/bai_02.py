import math
n = int(input("Nhập n (số nguyên dương): "))
# a)
S_1 = 0
i = 1
while i <= n:
    S_1 += ((-1)**(i+1))/i
    i += 1
print(f"S_A = {S_1}")

# b) 
S_2 = 0
i = 1
while i <= n:
    S_2 +=1 /(i*(i+1))
    i += 1
print(f"S_B = {S_2}")

# c)
S_3 = 0
i = 2
while i <= n:
    S_3 += 1/math.sqrt(i)
    i += 1
print(f"S_C = {S_3}")