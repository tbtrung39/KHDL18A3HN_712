m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
for i in range(m):
    hang=list(map(int,input(f"Nhập hàng {i+1}: ").split()))
    A.append(hang)
total_sum = sum(sum(hang) for hang in A)
print("Ma trận A: ")
for hang in A:
    print(hang)
print("Tổng các phần tử của ma trận A:", total_sum)