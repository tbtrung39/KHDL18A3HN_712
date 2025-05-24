import random,math

def sinh_day_so():
    n=random.randint(1,100)
    return [random.randint(0,1000) for _ in range(n)]

def la_so_nguyen_to(x):
    if x<2: return False
    for i in range(2,int(math.isqrt(x))+1):
        if x%i==0: return False
    return True

def so_nguyen_to_chia_het_7(day):
    return [x for x in day if la_so_nguyen_to(x) and x%7==0]

def tong_so_le(day):
    return sum(x for x in day if x%2==1)

def so_chinh_phuong(day):
    return [x for x in day if int(math.isqrt(x))**2==x]
