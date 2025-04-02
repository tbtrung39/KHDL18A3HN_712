X = int(input("Nhap so hang X: "))
Y = int(input("Nhap so cot Y: "))
ma_tran=[]
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i*j)
    ma_tran.append(hang)
print("Ma tran in ra:")
for hang in ma_tran:
    print(hang)