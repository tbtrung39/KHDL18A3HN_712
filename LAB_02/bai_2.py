a,b,c = map(float,input("nhập giá trị của a,b,c:").split(','))
fx = b**2 -4*a*c
if fx < 0:
    print("phương trình vô nghiệm")
elif fx ==0 :
    x = -b/(2*a)
    print("nghiện của phương trình là:",x)
elif fx>0:
    import math
    x1 = (-b+math.sqrt(fx))/2*a
    x1 = (-b-math.sqrt(fx))/2*a
    print("nghiệm đầu tiên của phương trình là x1=%0.2f và x2=%0.2f")