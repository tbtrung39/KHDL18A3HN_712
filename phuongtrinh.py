#Bai 4
import math
def phuongTrinhBacNhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh vo nhiem"
    else:
        x = -b / a
        return f"nghiem x = {x}"

def phuongTrinhBacHai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phuong trinh co 2 nghiem phan biet: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phuong trinh co nghiem kep : x = {x}"
    else:
        return "Phuong trinh vo nghien ."