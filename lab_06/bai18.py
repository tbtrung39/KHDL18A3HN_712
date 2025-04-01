# Nhập số hàng và số cột của ma trận
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

ma_tran_a = []
for i in range(m):
    hang = []
    for j in range(n):
        while True:
            try:
                phan_tu = int(input(f"Nhập phần tử a[{i}][{j}]: "))
                hang.append(phan_tu)
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên.")
    ma_tran_a.append(hang)

print("Ma trận A:")
for hang in ma_tran_a:
    print(hang)

tong = 0
for hang in ma_tran_a:
    for phan_tu in hang:
        tong += phan_tu
print("Tổng các phần tử của ma trận A:", tong)