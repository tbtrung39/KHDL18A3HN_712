# bai 7
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# In các phần tử của List_ ra màn hình
print("Danh sách List_:")
for item in List_:
    print(item)

# Chọn ra phần tử thứ hai, thuộc vị trí thứ 3 của sublist
phan_tu_thu_2_thu_3 = List_[2][1]
print("\nPhần tử thứ hai, thuộc vị trí thứ 3 của sublist:", phan_tu_thu_2_thu_3)

# Kiểm tra độ dài của danh sách test và thêm một sublist ngẫu nhiên
test = List_
print("\nĐộ dài của danh sách test:", len(test))
# Thêm một sublist ngẫu nhiên (ví dụ thêm sublist ["sun", 130])
test.append(["sun", 130])
print("Danh sách test sau khi thêm sublist ngẫu nhiên:", test)

# Tính tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
cac_ngay_tinh_tong = ["mon", "tue", "sat", "sun"]
tong_sale_value = sum([item[1] for item in List_ if item[0] in cac_ngay_tinh_tong])
print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong_sale_value)