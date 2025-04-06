#Bai16
day_so = list(map(int, input("Nhập dãy số: ").split()))
cap_chi_so = []
n = len(day_so)
for i in range(n):
    for j in range(i + 1, n):
        if day_so[i] + 1 == day_so[j]:
            cap_chi_so.append((i, j))
print("Các cặp chỉ số:", cap_chi_so)