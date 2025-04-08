# bai 13
W = input("Hay nhap chuoi ky tu: ")

tu_dien = {}
n = len(W)
i = 0
while i < n:
    j = i + 1
    while j <= n:
        chuoi_con = W[i:j]
        if chuoi_con in tu_dien:
            tu_dien[chuoi_con] += 1
        else:
            tu_dien[chuoi_con] = 1
        j += 1
    i += 1

print("Tu đien cac chuoi con va so lan xuat hien:")
for k in tu_dien:
    print(k, ":", tu_dien[k])
