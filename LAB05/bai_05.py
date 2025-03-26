# cach 1
input_str = input("Nhap chuoi ky tu: ")
num_str = ""
for char in input_str:
    if char.isdigit():
        num_str += char
if num_str:
    num = int(num_str)
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    print(f"So sau khi loc: {num}")
    if sum_divisors == num:
        print("Day la so hoan hao.")
    else:
        print("Day khong phai so hoan hao.")
else:
    print("Khong co so nao trong chuoi dau vao.")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
num_str = "".join(filter(str.isdigit, input_str))
if num_str:
    num = int(num_str)
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    print(f"So sau khi loc: {num}")
    if sum_divisors == num:
        print("Day la so hoan hao.")
    else:
        print("Day khong phai so hoan hao.")
else:
    print("Khong co so nao trong chuoi dau vao.")
