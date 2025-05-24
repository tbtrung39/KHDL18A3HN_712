import math
def giai_pt_bac_nhat_1_an(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b / a
        return f"Phuong trinh co nghiem duy nhat la: x = {x}"
def giai_pt_bac_2(a, b, c):
    if a == 0:
        return giai_pt_bac_nhat_1_an(b, c)
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phuong trinh co nghiem kep la: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phuong trinh co hai nghiem phan biet la: x1 = {x1}, x2 = {x2}"