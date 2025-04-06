import random
n = int(input("Nhập số lượng phần tử trong tập hợp A: "))
A = {round(random.random() * 100, 1) for i in range(n)}
min_value = min(A)
max_value = max(A)
sum_value = round(sum(A), 1)
print("Tập hợp A: ", A)
print("Giá trị nhỏ nhất trong A:", min_value)
print("Giá trị lớn nhất trong A:", max_value)
print("Tổng các giá trị trong A:", sum_value)
