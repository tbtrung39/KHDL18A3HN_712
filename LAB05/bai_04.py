# cach 1
str1 = input("Nhap chuoi thu nhat: ")
str2 = input("Nhap chuoi thu hai: ")
result = ""
max_length = max(len(str1), len(str2))
for i in range(max_length):
    if i < len(str1):
        result += str1[i]
    if i < len(str2):
        result += str2[i]
print(f"Chuoi sau khi tron: {result}")
# cach 2
from itertools import zip_longest
str1 = input("Nhap chuoi thu nhat: ")
str2 = input("Nhap chuoi thu hai: ")
result = "".join(a + b for a, b in zip_longest(str1, str2, fillvalue=""))
print(f"Chuoi sau khi tron: {result}")
