list1 = [1, 2, 3, 4]
list2 = ["An", "Bình", "Chi", "Dũng"]

if len(list1) == len(list2):
    combined_dict = {list1[i]: list2[i] for i in range(len(list1))}
    print("Từ điển kết hợp từ hai danh sách:")
    print(combined_dict)
else:
    print("Hai danh sách không có cùng độ dài.")
