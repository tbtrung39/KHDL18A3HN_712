a=int(1)
tong1=0
while True:
    tong1 += ((-1)**(a+1))/a
    a += 1
    if a ==10:
        break
    print(tong1)