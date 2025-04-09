n = int(input("Hay nhap so tu nhien n tu ban phim: "))

print("So nguyen to dau tien la=:", n)

dem = 0     
so = 2       
while dem < n:
    la_so_nguyen_to = True

    if so < 2:
        la_so_nguyen_to = False
    else:
        i = 2
        while i < so:
            if so % i == 0:
                la_so_nguyen_to = False
                break
            i += 1
    if la_so_nguyen_to == True:
        print(so, end=" ")
        dem += 1
    so += 1