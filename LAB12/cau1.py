import math
def n(c):
    v=input(f"{c}:")
    if not v.replace('.','',1).isdigit() or float(v)<=0:raise ValueError("Cạnh phải số dương")
    return float(v)
def k(l):
    a,b,c=l
    if a+b<=c or a+c<=b or b+c<=a:raise ValueError("Ko phải tam giác")
def d(l):
    a,b,c=l
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
try:
    l=[n(i)for i in"abc"]
    print("List:",l)
    k(l)
    print(f"Diện tích:{d(l):.2f}")
except ValueError as e:print("Lỗi:",e)