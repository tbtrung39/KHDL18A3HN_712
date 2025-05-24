def uoc_nt(x):
    u=set()
    i=2
    while i*i<=x:
        while x%i<1:
            u.add(i)
            x//=i
        i+=1
    if x>1:u.add(x)
    return sorted(u)

duong_dan=input("Nhap duong dan tep f_in.dat:")
with open(duong_dan,"r")as f,open("f_out.dat","w")as g:
    for d in f:
        g.write(" ".join(map(str,uoc_nt(int(d))))+"\n")
