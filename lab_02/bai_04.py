n = int(input("Nhap so nguyen: "))
if n >= 100:
    n = (n//100) % 10
else:
    n = 0
print(f"Chu so hang tram cua {n} la: {n}")