x = int(input("Nhập ngày: "))
y = int(input("Nhập tháng: "))

if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
    ngay_cuoi = 31
elif y == 4 or y == 6 or y == 9 or y == 11:
    ngay_cuoi = 30
else:
    ngay_cuoi = 28

if x < ngay_cuoi and y < 12:
    ngay_sau = x +1
    thang_sau = y
elif y > ngay_cuoi and y < 12:
    ngay_sau = 1
    thang_sau = y+1
else:
    ngay_sau =1
    thang_sau =1  

print(f"Ngày tiếp theo: {ngay_sau}/{thang_sau}")

