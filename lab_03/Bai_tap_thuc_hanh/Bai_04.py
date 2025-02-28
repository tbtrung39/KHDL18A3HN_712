n=int(input("Nhập số nguyên n:"))
print("Các số nguyên tố nhỏ hơn hoặc bằng n là:")
for i in range(2,n+1):
    la_so_nguyen_to=True
    for j in range(2,i):
        if i%j==0:
            la_so_nguyen_to=False
    if la_so_nguyen_to:
        print(i,end=" ")