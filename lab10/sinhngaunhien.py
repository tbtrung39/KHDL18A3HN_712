import random
import math

def sinh_ngau_nhien(max_length=100, max_value=100):
    length = random.randint(1, max_length)
    return [random.randint(0, max_value) for _ in range(length)]

def tong_cac_so_le(arr):
    return sum(num for num in arr if num % 2 == 1)

def so_nguyen_to_chia_het_cho_7(arr):
    def la_so_nguyen_to(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return [num for num in arr if num % 7 == 0 and la_so_nguyen_to(num)]

def so_chinh_phuong(arr):
    so_chinh_phuong = [num for num in arr if math.isqrt(num)**2 == num]
    return so_chinh_phuong
