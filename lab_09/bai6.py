import random
def hoanvi(A):
    if not A:return[]
    x=random.choice(A)
    A.remove(x)
    return [x]+hoanvi(A)

n=int(input("Nhập số tự nhiên n:"))
print(hoanvi(list(range(1,n+1))))