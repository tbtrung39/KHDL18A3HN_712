import random
import math
def sinh_day_so():
    n = random.randint(1, 100)  
    day_so = [random.randint(1, 100) for _ in range(n)]  
    print("dso da sinh ngau nhien:", day_so)
    return day_so

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_chia_het_7(day_so):
    primes_div_7 = [x for x in day_so if la_so_nguyen_to(x) and x % 7 == 0]
    print("cac so nguyen to chia het cho 7:", primes_div_7)

def tong_so_le(day_so):
    tong = sum(x for x in day_so if x % 2 != 0)
    print("tong cac so le trong day y:", tong)

def so_chinh_phuong(day_so):
    chinh_phuong = [x for x in day_so if math.isqrt(x)**2 == x]
    if chinh_phuong:
        print("cac so chinh phuong trong day la:", chinh_phuong)
    else:
        print("ko co so chinh phuong.")
