#Bai16
x=int(input("Nhập X: "))
y=int(input("Nhập Y: "))
bang=[]
for i in range(x):
    row=[]
    for j in range(y):
        row.append(i*j)
    bang.append(row)
print("Kết quả:")
for row in bang:
    print(row)