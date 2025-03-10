n = int(input("Nhập n"))
i = 1
#a,
tong = 0 
while i<=n:
    tong += (-1)**(i+1)/i
    i +=1
print(tong)
#b,
tong1 = 0
while i<=n:
    tong1 += 1/((i)*(i+1))
    i+= 1
print(tong1)
#c,
tong3 = 0
while i <= n:
    tong3 += 1/((i+1)**1/2)
    i += 1
print(tong3)
