vector_a = list(map(float, input("Nhập vector a : ").split()))
vector_b = list(map(float, input("Nhập vector b : ").split()))
tich_vo_huong = sum(a * b for a, b in zip(vector_a, vector_b))
print(f"Tích vô hướng của hai vector: {tich_vo_huong}")
