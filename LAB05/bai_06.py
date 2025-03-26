# cach 1
input_str = input("Nhap chuoi ky tu: ")
if input_str == input_str[::-1]:
    print("Day la chuoi doi xung.")
else:
    print("Day khong phai chuoi doi xung.")
# cach 2
input_str = input("Nhap chuoi ky tu: ")
is_palindrome = True
for i in range(len(input_str) // 2):
    if input_str[i] != input_str[-(i + 1)]: 
        is_palindrome = False
        break  
if is_palindrome:
    print("Day la chuoi doi xung.")
else:
    print("Day khong phai chuoi doi xung.")
