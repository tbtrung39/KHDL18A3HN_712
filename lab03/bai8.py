n = int(input("Nhập n: "))
if n <= 0:
    n = int(input("n phải lớn hơn 0. Vui lòng nhập lại n: "))
# a) 
S1 = n * (n + 1) // 2
print(f"Tổng S1 = {S1}")
# b) 
S2 = (n + 1) ** 2
print(f"Tổng S2 = {S2}")
# c) 
S3 = n * (n + 1)
print(f"Tổng S3 = {S3}")