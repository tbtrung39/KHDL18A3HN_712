def double_factorial(n):
    # Tính giai thừa kép n!! không sử dụng đệ quy
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

def calculate_sum(k):
    total_sum = 0
    for i in range(1, k + 1):
        if i % 2 == 0:  # Nếu i là số chẵn
            total_sum -= double_factorial(i)
        else:  # Nếu i là số lẻ
            total_sum += double_factorial(i)
    return total_sum

# Tính tổng S với k < 1000
k = 999  # k < 1000
result = calculate_sum(k)

# In kết quả mà không sử dụng f-string
print("Tổng S = 1!! - 2!! + 3!! - 4!! + ... + (-1)^" + str(k) + " k!! với k = " + str(k) + " là: " + str(result))