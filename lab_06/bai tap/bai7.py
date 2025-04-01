import random
List_ = [
    ["mon", 73], 
    ["tue", 89], 
    ["wed", 95], 
    ["thu", 103], 
    ["fri", 115], 
    ["sat", 128],
    ["sun", 120]
]

print("Các phần tử của List_:")
for item in List_:
    print(item)

element = List_[2][1]
print("\nPhần tử thứ hai của sublist thứ 3:", element)

print("\nĐộ dài ban đầu của List_:", len(List_))

new_day = random.choice(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
new_sale_value = random.randint(50, 150)
new_sublist = [new_day, new_sale_value]

List_.append(new_sublist)

print("\nDanh sách List_ sau khi thêm sublist ngẫu nhiên:")
for item in List_:
    print(item)
days_to_check = ["mon", "tue", "sat", "sun"]
total_sales = 0
for day, sale in List_:
    if day in days_to_check:
        total_sales += sale

print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", total_sales)
