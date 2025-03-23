binary_str = input("Nhập chuỗi nhị phân: ")
decimal = 0  
power = 0  
for i in range(len(binary_str) - 1, -1, -1): 
    if binary_str[i] == '1':  
        decimal += 2 ** power 
    power += 1 
print("Giá trị thập phân:", decimal)
