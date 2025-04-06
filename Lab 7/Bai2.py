#Bai2
import random
numbers = list(map(int, input("Nhập số tự nhiên: ").split()))
A = set()
while len(A) < len(numbers):  # //2:
    A.add(numbers[random.randint(0, len(numbers)-1)])
print("Danh sách Numbers:", numbers)
print("Tập hợp A:", A)