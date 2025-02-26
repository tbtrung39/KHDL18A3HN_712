thang = int(input("Nhập vào một tháng (1-12): "))

if thang == [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang == [4, 6, 9, 11]:
    so_ngay = 30
elif thang == 2:
    so_ngay = 28
else:
    so_ngay = None

if so_ngay:
    print(f"Tháng {thang} có {so_ngay} ngày.")
else:
    print("Tháng không hợp lệ!")
