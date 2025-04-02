#Bai17
n = int(input("Nhập bậc của ma trận: "))
ma_tran = []
for i in range(n):
    hang = [] 
    for j in range(n):
        hang.append(0) 
    ma_tran.append(hang) 
for i in range(n):
    ma_tran[i][i] = 1
for hang in ma_tran:
    print(hang)