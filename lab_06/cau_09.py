lst = [2, 4, 6, 8, 10]
assert all(x % 2 == 0 for x in lst), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")

lst2 = [2, 4, 5, 8]
assert all(x % 2 == 0 for x in lst2), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")
