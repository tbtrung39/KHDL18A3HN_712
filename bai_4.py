import phuongtrinh 

print("Hay chon loai phuong trinh:")
print("1. Phuong trinh bac nhat")
print("2. Phuong trinh bac 2")

choice = int(input("Hay nhap lua chon cua ban: "))

if choice == 1:
    a = float(input("Nhap a tu ban phim: "))
    b = float(input("Nhap b tu ban phim: "))
    print(phuongtrinh.phuongTrinhBacNhat(a, b))
elif choice == 2:
    a = float(input("Nhap a tu ban phim: "))
    b = float(input("Nhap b tu ban phim: "))
    c = float(input("Nhap c tu ban phim: "))
    print(phuongtrinh.phuongTrinhBacHai(a, b, c))
else:
    print("Khong hop le")