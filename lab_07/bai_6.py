n = int(input("Nhap so nguyen n: "))

dem = 0
so = 2
day_nt = []

while dem<n:
    la_nt = True
    for i in range(2, int(so**0.5) + 1):
        if so%i == 0:
            break
    if la_nt:
        day_nt.append(so)
        dem += 1
    so += 1

print("Day", n, "so nguyen to dau tien: ")
print(day_nt)