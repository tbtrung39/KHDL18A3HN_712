m, n = map(int, input("Nhap so hang m va so cot n: ").split())

A = []
for i in range(m):
    row = list(map(int, input(f"Nhap {n} so cho hang {i + 1}, cach nhau boi dau cach: ").split()))
    while len(row) != n:
        print(f"Hang {i + 1} phai co dung {n} so. Vui long nhap lai.")
        row = list(map(int, input(f"Nhap {n} so cho hang {i + 1}, cach nhau boi dau cach: ").split()))
    A.append(row)

tong = sum(sum(row) for row in A)
print("Tong cac phan tu cua ma tran A la:", tong)