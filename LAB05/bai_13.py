# cach 1
input_str = input("Nhap chuoi ky tu: ")
result = input_str.replace(" ", "_")
print(f"Chuoi sau khi thay the: {result}")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
result = ""
for char in input_str:
    if char == " ":
        result += "_"
    else:
        result += char
print(f"Chuoi sau khi thay the: {result}")
