import random
chars_input = input("Nhập các ký tự (chữ và số, không cách): ")
n = random.randint(1, len(chars_input))
m = random.randint(1, len(chars_input))
A = set(random.sample(chars_input, n))
B = set(random.sample(chars_input, m))

print("Tập hợp A:", A)
print("Tập hợp B:", B)

phan_tu_chung = A & B
print("Phần tử chung của A và B:", phan_tu_chung)
