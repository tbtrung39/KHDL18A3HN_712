import random
A=set(input("Nhập các ký tự cho tập hợp A (không có dấu cách giữa các ký tự): "))
B=set(input("Nhập các số cho tập hợp B (không có dấu cách giữa các số): "))
A={random.choice(list(A))for _ in range(len(A))}
B={random.choice(list(B))for _ in range(len(B))}
phantu_chung=A.intersection(B)
print("Tập hợp A:",A)
print("Tập hợp B:",B)
print("Phần tử chung của A và B:",phantu_chung)