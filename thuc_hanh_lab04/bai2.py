#a
import math 
S1 = 0
for i in range(1, 100):
    if i % 2 == 1:
        S1 += 1 / i
    else:
        S1 -= 1 / i
print("Tổng S1:", S1)
# b
S2 = 0
for i in range(2, 100):
    S2 += 1 / (i * (i + 1))
print("Tổng S2:", S2)

#c 
S3 = 0
for i in range(2, 100):
    S3 += 1 / (i ** (1/2))  
print("Tổng S3:", S3)