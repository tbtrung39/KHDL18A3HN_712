n=int(input("nhập số: "))
tong=0
while n>0:
    tong+=(n%10)
    n=n//10
print(f"tổng chữ số của số là: {tong}")