n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]


result_a = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách các phần tử chia hết cho 3 nhưng không chia hết cho 5:", result_a)

C = [x**2 for x in A]

print("Danh sách C (bình phương của A):", C)

D = [x for x in A if x % 12 == 0]

print("Danh sách D (các phần tử chia hết cho 12):", D)