n = int(input("Nhập n: "))
tong = 1  
tich = 1  

for i in range(1, n+1):
    tich *= (2*i)/(2*i+1)
    tong += tich

print(f"Tổng dãy số S = {tong:.3f}")
