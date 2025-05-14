import random
import math
def sinh_day_so(n):
    return [random.randint(0, 1000) for _ in range(n)]
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def liet_ke_nt_chia_het_cho_7(day):
    return [x for x in day if so_nguyen_to(x) and x % 7 == 0]
def tinh_tong_so_le(day):
    return sum(x for x in day if x % 2 != 0)
def kiem_tra_so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n
def co_chinh_phuong(day):
    ds = [x for x in day if kiem_tra_so_chinh_phuong(x)]
    return ds if ds else "Khong co so chinh phuong trong day"
