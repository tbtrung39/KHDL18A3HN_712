# cach 1
input_str = input("Nhap chuoi ky tu: ")
reversed_str = " ".join(input_str.split()[::-1])
print(f"Chuoi sau khi dao nguoc: {reversed_str}")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
words = input_str.split()
reversed_str = ""
for i in range(len(words) - 1, -1, -1):
    reversed_str += words[i] + " "
print(f"Chuoi sau khi dao nguoc: {reversed_str.strip()}")
