#Bai3 
#Kiểm tra n có phải số nguyên tố không 
n=int(input("Nhập số nguyên dương n:")) 
kiem_tra=1 
if n<2: 
    kiem_tra=0 
else: 
    for i in range(2,int(n**0.5)+1): 
        if n%i==0: 
            kiem_tra=i 
            break 
if kiem_tra==1: 
    print(n,"là số nguyên tố") 
else: 
    print(n,"không là số nguyên tố") 
#In số nguyên tố gần nhất với n 
 #Số nguyên tố lớn hơn n 
so_lon_hon=n+1 
for i in range(n+1,n+100): 
    kiem_tra=1 
    for j in range(2,int(i**0.5)+1): 
        if i%j==0: 
            kiem_tra=0 
            break 
    if kiem_tra==1: 
        so_lon_hon=i 
        break 
 #Số nguyên tố bé hơn n 
so_be_hon=n-1 
for i in range(n-1,-1): 
    kiem_tra=1 
    for j in range(2,int(i**0.5)+1): 
        if i%j==0: 
            kiem_tra=0 
            break 
    if kiem_tra==1: 
        so_be_hon=i 
        break 
if n-so_be_hon<=so_lon_hon-n: 
    print("Số nguyên tố gần nhất với",n,"là:",so_be_hon) 
else: 
    print("Số nguyên tố gần nhất với",n,"là:",so_lon_hon)