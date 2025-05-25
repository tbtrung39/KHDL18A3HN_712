def tinh_dien_tich_tam_giac(a,b,c):
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("ba canh khong thoa man dieu kien")
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))** 0.5
    return area
while True:
    try:
        a=float(input("Nhap canh a: "))
        b=float(input("Nhap canh b: "))
        c=float(input("Nhap canh c: "))
        if a<=0 or b<=0 or c<=0:
            raise ValueError("cac canh phai la so duong lon 0")
        area = tinh_dien_tich_tam_giac(a,b,c)
        print(f"dien tich tam giac la:{area:.2f}")
        break
    except ValueError as ve:
        print(f"loi:{ve}")
    except Exception:
        print("loi khong xac dinh. vui long thu lai")