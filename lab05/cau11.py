#Cach 1:
binary = input("Nhap chuoi nhi phan: ")
nhi_phan = 0
gt = 0

for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1':
        nhi_phan += 2 ** gt
    gt += 1

print(f"Gia tri he 10: {nhi_phan}")

#Cach 2;
binary_str = input("Nhap chuoi nhi phan: ")
decimal_value = int(binary_str, 2)  
print(f"Gia tri he 10: {decimal_value}")