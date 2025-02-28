n=int(input("Nhập giá trị n:"))
Tong=1
for i in range(1,n+1):
    tich=1
    for j in range(1,n+1):
        tu_so=2*j
        mau_so=2*j+1
        tich=tu_so/mau_so
Tong += tich
print(f"Kết quả của biểu thức là:{round(Tong,3)}")