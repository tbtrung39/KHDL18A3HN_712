n=int(input('Nhập số tự nhiên n: '))
so_nguyen_to=[]
tap_hop=set()
so=2
while len(so_nguyen_to)<n:
    if so not in tap_hop:
        so_nguyen_to.append(so)
        for i in range(2*so,10**6,so):
            tap_hop.add(i)
    so=so+1
print('Dãy',n,"Số nguyên tố đầu tiên:",so_nguyen_to)
