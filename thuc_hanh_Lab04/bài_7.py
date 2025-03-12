a = int(input("Nhập a : "))
b = int(input("Nhập b : "))
if a > b:
    bcnn = a
else:
    bcnn = b      
while not (bcnn % a == 0 and bcnn % b == 0):  
    bcnn += 1  
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")
