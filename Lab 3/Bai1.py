#Bai1 
n=int(input("Nhập n:")) 
tong=1 
tich=1 
for i in range(1,n+1): 
    tich*=(i*2)/(i*2+1) 
    tong+=(tich) 
print("Kết quả của phép toán là:",round(tong,3))