n=int(input("nhập số "))
s4 = 0
for i in range(1, n + 1):
    s4 += i ** 2
print("s4 = ", s4)

s5 = 0
for i in range(n + 1):
    s5 += (2*i + 1) ** 3
print("s5 = ", s5)

s6 = 0
for i in range(1, n + 1):
    s6 += (2*i) ** 4
print("s6 = ",s6)