# bai 4
import phuongtrinh 

print("hay chon loai phuong trinh:")
print("1. pt bac nhat")
print("2. pt bac 2")

choice = int(input("hay nhap lua chon cua ban: "))

if choice == 1:
    a = float(input("nhap a tu ban phim: "))
    b = float(input("nhap b tu ban phim: "))
    print(phuongtrinh.phuongTrinhBacNhat(a, b))
elif choice == 2:
    a = float(input("nhap a tu ban phim: "))
    b = float(input("nhap b tu ban phim: "))
    c = float(input("nhap c tu ban phim: "))
    print(phuongtrinh.phuongTrinhBacHai(a, b, c))
else:
    print("khong hop le")