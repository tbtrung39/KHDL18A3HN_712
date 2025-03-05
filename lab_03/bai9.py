n = int(input("Nhập n: "))
if n <= 0:
    n = int(input("n phải lớn hơn 0 nhập lại n: "))
#a
S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print(S4)
#b 
S5 = 1
for i in range(1, n + 1):
    S5 += (2 * i + 1) ** 3
print(S5)
#c 
S6 = 0
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print(S6)