import my_Triangle
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
if my_Triangle.ktra_tam_giac(a,b,c):
    print("Ba canh tao thanh mot tam giac.")
    print("Chu vi tam giac la:",my_Triangle.chu_vi_tam_giac(a,b,c))
    print("Dien tich tam giac la:",my_Triangle.dien_tich_tam_giac(a,b,c))
else:
    print("Ba canh khong tao thanh mot tam giac!")