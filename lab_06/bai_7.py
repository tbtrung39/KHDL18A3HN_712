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

print("Cac phan tu cua List_:")
for item in List_:
    print(item)

element = List_[2][1]
print("\nPhan tu thu hai cua sublist thu 3:", element)

print("\nDo dai ban dau cua List_:", len(List_))

new_day = random.choice(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
new_sale_value = random.randint(50, 150)
new_sublist = [new_day, new_sale_value]

List_.append(new_sublist)

print("\nDanh sach List_ sau khi them sublist ngau nhien:")
for item in List_:
    print(item)
days_to_check = ["mon", "tue", "sat", "sun"]
total_sales = 0
for day, sale in List_:
    if day in days_to_check:
        total_sales += sale

print("\nTong sale value trong các ngay thu hai, thu ba, thu bay va chu nhat:", total_sales)