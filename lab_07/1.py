my_set = set()
while True:
    n = input("Nhập n (nhập 'q' để thoát): ")
    if n == "q":
        break
    else:
        my_set.add(n)
print("Tập hợp ban đầu:", my_set)
for i in list(my_set):
    if i.isdigit():
        removed = my_set.pop()
        print(f"Đã xóa phần tử: {removed}")
    else:
        my_set.add("không hợp lệ")
print("Tập hợp sau xử lý:", my_set)