import math
x = int(input("nhập giá trị n:"))
epsilon = 1e-4 
i = 1
S = 1
cos = S
n = 1
while i<epsilon :
    S = -x**2 / (2*n * (2*n - 1))
    cos += S
    n += 1
print(f"giá trị sấp xỉ cos({x}) là:{cos}")
print(f"giá trị thực của cos({x}) là:{math.cos(x)}")
