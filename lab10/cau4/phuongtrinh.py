import math

def Pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b / a
        return f"Nghiem cua pt la x: {x}"

def Pt_bac_hai(a, b, c):
    if a == 0:
        return Pt_bac_nhat(b, c)

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phuong trinh co nghiem kep x: {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phuong trinh co 2 nghiem phan biet: x1 = {x1}, x2 = {x2}"