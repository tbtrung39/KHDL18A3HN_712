def find_combinations(n, N, current_combination, results):
    # Nếu tổng hiện tại bằng N, lưu lại bộ nghiệm
    if N == 0:
        results.append(current_combination.copy())
        return
    
    # Nếu tổng hiện tại lớn hơn 0 và còn số phần tử cần tìm
    if N > 0 and len(current_combination) < n:
        for i in range(1, N + 1):  # Bắt đầu từ 1 đến N
            current_combination.append(i)
            find_combinations(n, N - i, current_combination, results)
            current_combination.pop()  # Quay lại để thử nghiệm với số khác

# Nhập số tự nhiên n và tổng N từ bàn phím
n = int(input("Nhập số tự nhiên n: "))
N = int(input("Nhập tổng N: "))

results = []
find_combinations(n, N, [], results)

# In ra tất cả các bộ nghiệm
print(f"Tất cả các bộ nghiệm của phương trình N = x1 + x2 + ... + x{n}:")
for combination in results:
    print(combination)