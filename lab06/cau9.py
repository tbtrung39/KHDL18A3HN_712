numbers = [2, 4, 6, 8, 10]
assert all(num % 2 == 0 for num in numbers), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")