x = float(input("Nhập số x: "))
log4_x = (x ** (1/4) - 1) * 4
logx_2 = (2 ** (1/x) - 1) * x 
bt = log4_x + logx_2
print(f"Giá tri của biểu thức: {bt:.2f}")