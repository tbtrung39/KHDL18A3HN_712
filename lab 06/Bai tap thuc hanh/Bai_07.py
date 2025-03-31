List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Danh sách List_:")
for sublist in List_:
    print(sublist)

print(List_[3][1])

print("\nĐộ dài của List_:", len(List_))
List_.append(["random", 50])
print("\nDanh sách List_ sau khi thêm:")
print(List_)

days = ["tue", "wed", "sat", "sun"]
total_sales = sum(sales for day, sales in List_ if day in days)

print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", total_sales)