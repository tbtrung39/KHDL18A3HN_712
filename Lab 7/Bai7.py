#Bai7
import random
so_pt_A = int(input("Nhập số phần tử của A: "))
so_pt_B = int(input("Nhập số phần tử của B: "))
chu_cai = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
so = "0123456789"
A = set()
while len(A) < so_pt_A:
    A.add(random.choice(chu_cai + so))
B = set()
while len(B) < so_pt_B:
    B.add(random.choice(chu_cai + so))
print("Tập hợp A:", A)
print("Tập hợp B:", B)
phan_tu_chung = A.intersection(B)
print("Các phần tử chung của A và B:", phan_tu_chung)