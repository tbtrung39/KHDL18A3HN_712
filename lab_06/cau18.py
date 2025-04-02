m,n=int(input("nhap so dong: ")), int(input("nhap so cot :"))
tong=0
for i in range(m):
    for j in range(n):
        tong+=int(input(f"nhap phan tu thu ({i+1},{j+1}): "))
print("tong cac phan tu trong ma tran la:", tong)