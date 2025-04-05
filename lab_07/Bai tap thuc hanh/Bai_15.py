list1 = input("Nhập danh sách list1: ").split(',')
list1 = [int(x.strip()) for x in list1]

list2 = input("Nhập danh sách list2: ").split(',')
list2 = [x.strip() for x in list2]

if len(list1) != len(list2):
    print("Lỗi: Hai danh sách có độ dài không bằng nhau.")
else:
    tu_dien = {}
    for i in range(len(list1)):
        tu_dien[list1[i]] = list2[i]
    print("Từ điển kết quả:")
    for a, ten in tu_dien.items():
        print(f"{a}: {ten}")