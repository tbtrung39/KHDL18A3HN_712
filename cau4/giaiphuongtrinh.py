import math
def giai_bac_nhat(a, b):
    if a == 0:
        return "Vo nghiem" if b != 0 else "Vo so nghiem"
    return -b / a
def giai_bac_hai(a, b, c):
    if a == 0:
        return giai_bac_nhat(b, c)
    delta = b**2 - 4 * a * c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phuong trinh co nghiem kep x = {x}"
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return f"Phuong trinh co hai nghiem x1 = {x1}, x2 = {x2}"
