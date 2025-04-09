import random

chuoi_ky_tu = input("Nhap chuoi ky tu chu va so (khong dau cach): ")
so_lg_A = input("Nhap so luong phan tu A: ")
so_lg_B = input("Nhap so luong phan tu B: ")

A = random.sample(chuoi_ky_tu, min(so_lg_A), len(chuoi_ky_tu))
B = random.sample(chuoi_ky_tu, min(so_lg_B), len(chuoi_ky_tu))

chung = list(set(A)&set(B))

print("Tap hop A:", A)
print("Tap hop B:", B)
print("Phan tu chung A & B:", chung)