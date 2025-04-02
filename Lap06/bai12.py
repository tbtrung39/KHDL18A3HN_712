gd = input("Nhập nhật ký giao dịch (D là nạp tiền, W là rút tiền): ").split()
 bd = 0
 for i in range(0, len(gd), 2):
     hd = gd[i]
     dem = int(gd[i + 1])
 
     if hd == 'D':  
         bd += dem
     elif hd == 'W':  
         bd -= dem
 print("Số dư cuối cùng trong tài khoản:", bd)