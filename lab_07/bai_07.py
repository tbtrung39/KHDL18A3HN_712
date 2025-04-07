import random
chars_input = input("Nhap cac ky tu(chu va so, khong cach): ")
n = random.randint(1, len(chars_input))
m = random.randint(1, len(chars_input))
A = set(random.sample(chars_input, n))
B = set(random.sample(chars_input, m))
print("Tap hop A: ", A)
print("Tap hop B: ", B)
phan_tu_chung = A & B
print("Cac phan tu chung cua A va B: ", phan_tu_chung)