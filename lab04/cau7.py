a=int(input("nhập số nguyên thứ nhất: "))
b=int(input("nhập số nguyên thứ 2: "))
if a>b:
    bcnn=a
else:
    bcnn=b

while bcnn%a!=0 or bcnn%b!=0:
    bcnn+=1
if bcnn%a==0 and bcnn%b==0:
    print(f"bội chung nhỏ nhất của {a} và {b} là {bcnn}")
    