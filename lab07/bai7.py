import random

s = input("Nhập chuỗi ký tự (chữ và số): ")
s = list(set(s))  
random.shuffle(s)

A = set(random.sample(s, min(len(s), random.randint(2, len(s)))))
B = set(random.sample(s, min(len(s), random.randint(2, len(s)))))

print("Tập hợp A:", A)
print("Tập hợp B:", B)
print("Phần tử chung A & B:", A & B)
