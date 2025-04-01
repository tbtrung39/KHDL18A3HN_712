numbers = list(map(int, input("Nhập danh sách các số, tách biệt bởi dấu cách: ").split()))

assert all(num % 2 == 0 for num in numbers), "Không phải tất cả các số đều là số chẵn!"

print("Tất cả các số trong danh sách đều là số chẵn.")