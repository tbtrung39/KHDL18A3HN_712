n = int(input("Hay nhap so nguyen n= "))
tu_dien = {}
i = 1
while i <= n:
    tu_dien[i] = i * i
    i += 1

print("Tu dien chua (i, i*i) la=:")
print(tu_dien)