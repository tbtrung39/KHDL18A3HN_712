m,n=int(input("nhập số dòng: ")), int(input("nhập số cột: :"))
tong=0
for i in range(m):
    for j in range(n):
        tong+=int(input(f"nhập phần tư thứ ({i+1},{j+1}): "))
print("tổng các phần tử trong ma trận là:", tong)