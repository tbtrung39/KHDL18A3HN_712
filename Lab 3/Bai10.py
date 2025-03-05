#Bai10 
n=int(input("Nhập số nguyên dương n:")) 
for i in range(2,n+1): 
    for j in range(n%i==0):   
        print(i,end='') 
        n //= i 
    for j in range(n%i==0):   
        print(i,end='') 
        n //= i 