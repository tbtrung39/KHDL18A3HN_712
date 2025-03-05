#Bai4 
n=int(input("Nhập số nguyên dương n:")) 
print("Các số nguyên tố bé hơn hoặc bằng n là:") 
for i in range(2,n+1): 
    kiem_tra=1 
    for j in range(2,int(i**0.5)+1): 
        if i%j==0: 
            kiem_tra=0 
            break 
if kiem_tra==1: 
    print(i,end='')