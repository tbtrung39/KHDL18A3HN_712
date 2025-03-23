s = input("Nhập chuỗi ký tự: ")
num_str = ""
for char in s:
    if char.isdigit():
        num_str += char  

if num_str:
    num = int(num_str)  
    print("Chuỗi số sau khi lọc:", num)

    tong = 0
    for i in range(1, num):  
        if num % i == 0:
            tong += i  

    if tong == num:
        print(num, "là số hoàn hảo.")
    else:
        print(num, "không phải là số hoàn hảo.")
else:
    print("Chuỗi không chứa số nào.")
