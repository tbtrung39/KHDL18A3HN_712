m=int(input('Nhập giá trị m ='))
n=int(input('Nhập giá trị n ='))
if m<n:
   temp=m; m=n; n=temp
while(m!=n):
    p=m-n
    if p>n:m=p
    else:
        m=n
        n=p
print('UCLN=',m)