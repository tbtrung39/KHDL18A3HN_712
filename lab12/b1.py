import math
try:
    a=float(input("nhap canh a: "))
    b=float(input("nhap canh b: "))
    c=float(input("nhap canh c: "))
    if a<=0 or b<=0 or c<=0:
        raise ValueError("canh tam giac phai la so duong lon hon 0")
    if a+b<=c or a+c<=b or b+c<=a:
        raise ValueError("ba canh khong thoa man dieu kien ton tai cua tam giac")
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Dien tich tam giac la:", s)
except ValueError as v:
    print("Loi:", v)
except ValueError as e:
    print("Loi khong xac dinh", e)
