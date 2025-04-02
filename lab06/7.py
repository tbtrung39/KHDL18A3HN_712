List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách ban đầu:")
for item in List_:
    print(item)
element = List_[2][1]
print("\nPhần tử thứ hai của sublist thứ 3:", element)
print("\nĐộ dài ban đầu của List_:", len(List_))
import random
new_sublist = ["new_day", random.randint(50, 150)]
List_.append(new_sublist)
print("Đã thêm sublist ngẫu nhiên:", new_sublist)
print("Độ dài sau khi thêm:", len(List_))
total_sales = List_[0][1] + List_[1][1] + List_[5][1] + List_[6][1]
print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", total_sales)