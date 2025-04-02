x=int(input("nhap so dong x: "))
y=int(input("nhap so cot y: "))
ma_tran=[]
for i in range(x):
    hang=[]
    for j in range(y):
        hang.append(i*j)
    ma_tran.append(hang)
print("ma tran da tao: ")
for hang in ma_tran:
    print(hang)