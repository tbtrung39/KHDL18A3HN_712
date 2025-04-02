m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
ma_tran_A = []
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        hang.append(phan_tu)
    ma_tran_A.append(hang)
tong = 0
for hang in ma_tran_A:
    for phan_tu in hang:
        tong += phan_tu
print("Tổng các phần tử của ma trận A:", tong)