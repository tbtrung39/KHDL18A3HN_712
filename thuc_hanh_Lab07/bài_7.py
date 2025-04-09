import random
chuoi = input("Nhập các ký tự chữ và số (ví dụ: abc123xyz): ")
ds_ky_tu = list(set(chuoi))  
A = set()
while len(A) < min(5, len(ds_ky_tu)):
    A.add(random.choice(ds_ky_tu))
B = set()
while len(B) < min(5, len(ds_ky_tu)):
    B.add(random.choice(ds_ky_tu))
print("Tập A:", A)
print("Tập B:", B)
chung = A & B
print("Phần tử chung của A và B:", chung if chung else "Không có phần tử chung")
