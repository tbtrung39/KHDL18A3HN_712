n = int(input("Nhập số n: "))
ma_tran_don_vi = [[0] * n for i in range(n)]
for i in range(n):
    ma_tran_don_vi[i][i] = 1
print("Ma trận đơn vị bậc", n, "là:")
for hang in ma_tran_don_vi:
    print(hang)