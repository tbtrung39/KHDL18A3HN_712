list1 = ["ten1", "ten2", "ten3"]
list2 = ["toan", "anh", "tin"]
d = dict(zip(list1, list2))
print("Từ điển tạo ra từ 2 danh sách:")
for k, v in d.items():
    print(k, "→", v)