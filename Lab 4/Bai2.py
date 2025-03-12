#Bai2
#a
n=int(input("Nhập số nguyên dương n (câu a):"))  
if n<=0:  
    print("Nhập sai, vui lòng nhập lại!")  
else:  
    tong_a=0  
    for i in range(1,n+1):  
        if i%2==0:  
            tong_a -= 1/i  
        else:  
            tong_a += 1/i  
    print("Sa=",tong_a)  
#b  
n=int(input("Nhập số nguyên dương n (câu b):"))  
if n<=0:  
    print("Nhập sai, vui lòng nhập lại!")  
else:  
    tong_b=0  
    i=1  
    while i<=n:  
        tong_b += 1/(i*(i+1))  
        i += 1  
    print("Sb=",tong_b)  
#c  
n=int(input("Nhập số nguyên dương n (câu c):"))  
if n<=0:  
    print("Nhập sai, vui lòng nhập lại!")  
else:  
    tong_c=0  
    i=2  
    while i<=n:  
        tong_c += 1/(i**0.5)  
        i += 1  
    print("Sc=",tong_c)