numbers = list(map(int, input("Nhap danh sach cac so (tach biet boi dau cach): ").split()))

assert all(num%2 == 0 for num in numbers), "Khong phai tat ca cac so deu la so chan!"

print("Tat ca cac so trong danh sach deu la so chan.")