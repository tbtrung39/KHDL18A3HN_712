import math
def phuongTrinhBacNhat(a, b):
    if a == 0:
        if b == 0:
            return "pt vs nghiem"
        else:
            return "pt vo nhiem"
    else:
        x = -b / a
        return f"nghiem x = {x}"

def phuongTrinhBacHai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"pt co 2 nghiem pb: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"pt co nghiem kep : x = {x}"
    else:
        return "Pt vo nghien ."
