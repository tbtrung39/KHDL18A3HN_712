w = input("Nhập vào chuỗi ký tự: ")
substring_dict = {}

for i in range(len(w)):
    for j in range(i+1, len(w)+1):
        sub = w[i:j]
        substring_dict[sub] = substring_dict.get(sub, 0) + 1

print("Từ điển các chuỗi con và số lần xuất hiện:")
print(substring_dict)