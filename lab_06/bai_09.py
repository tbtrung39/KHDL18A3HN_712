n = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
assert all(num % 2 == 0 for num in n), "Danh sách chứa số lẻ!"
print("Danh sách hợp lệ:", n)
