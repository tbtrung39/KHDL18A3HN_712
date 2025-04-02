X,Y = map(int, input("Nhập X và Y : ").split())
mang_2d = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang_2d.append(hang)
print(mang_2d)