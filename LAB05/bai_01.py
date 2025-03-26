#cach 1
input_str = input("Nhap chuoi ky tu: ")
digit_count = 0
for char in input_str:
    if char.isdigit():
        digit_count += 1
print(f"so ky tu là so trong chuoi: {digit_count}")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
digit_count = sum(1 for char in input_str if char.isdigit())
print(f"So ky tu la so trong chuoi: {digit_count}")
