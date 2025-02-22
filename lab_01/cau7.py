#a*x**2+b*x*c
a=int(input("nhập vào giá trị a: "))
b=int(input("nhập vào giá trị b: "))
c=int(input("nhập vào giá trị c: "))
delta=b**2-4*a*c
x_dinh=(-b)/(2*a)
y_dinh=(-delta)/(4*a)
print("đỉnh của phương trình bậc 2 là (",round(x_dinh,2),",",round(y_dinh,2),")")
