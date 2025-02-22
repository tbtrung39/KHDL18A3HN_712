#Câu11
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng (1-12): "))
if 1< thang < 12 :
    print('Vui long nhập lại')
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    max_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    max_ngay = 30
elif thang == 2:
    max_ngay = 28 
if ngay < max_ngay:  
    ngay += 1
else: 
    ngay = 1
    if thang == 12: 
        thang = 1
    else:
        thang += 1
print("Ngày tiếp theo là:", ngay, "/", thang)