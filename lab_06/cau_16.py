X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))
ma_tran = [[i * j for j in range(Y)] for i in range(X)]
for hang in ma_tran:
    print(hang)