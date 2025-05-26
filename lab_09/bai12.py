def g(b,c):
    if b<0 or c<0:return
    if b+c==36 and 2*b+4*c==100:return b,c
    if b+c>36 or 2*b+4*c>100:return
    r=g(b+1,c)
    if r:return r
    return g(b,c+1)
r=g(0,0)
print(f"Ga:{r[0]} Cho:{r[1]}" if r else"Khong co ket qua")