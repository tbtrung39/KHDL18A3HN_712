n = int(input("Nhập n: "))
if n <= 0:
    n = int(input("n phải lớn hơn 0. Vui lòng nhập lại n: "))
# a) 
S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print(f"Tổng S4 = {S4}")
# b) 
S5 = 1
for i in range(1, n + 1):
    S5 += (2 * i + 1) ** 3
print(f"Tổng S5 = {S5}")
# c) 
S6 = 0
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print(f"Tổng S6 = {S6}")