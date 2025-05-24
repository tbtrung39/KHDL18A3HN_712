def giai_pt_bac_nhat(a,b):
    if a==0: return "Vô số nghiệm" if b==0 else "Vô nghiệm"
    return -b/a
def giai_pt_bac_hai(a,b,c):
    if a==0: return giai_pt_bac_nhat(b,c)
    d=b*b-4*a*c
    if d<0: return "Vô nghiệm"
    if d==0: return -b/(2*a)
    from math import sqrt
    r=sqrt(d)
    return ((-b+r)/(2*a),(-b-r)/(2*a))
