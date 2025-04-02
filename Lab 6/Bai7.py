#Bai7
import random
# a. Tạo danh sách List_ và in các phần tử của List_ ra màn hình
list_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách list_:")
for i in list_:
    print(i)
# b. Chọn ra phần tử thứ hai trong sublist thứ 3
pt_2_vtri_3 = list_[2][1]
print("Phần tử thứ hai trong sublist thứ 3:", pt_2_vtri_3)
# c. Kiểm tra độ dài của list_ và thêm một sublist ngẫu nhiên
print("Độ dài của list_ trước khi thêm:", len(list_))
random_gtri = random.randint(1, 200)
random_ngay = "random_ngay" 
ds_random = [random_ngay, random_gtri]
list_.append(ds_random)
print("Đã thêm danh sách ngẫu nhiên:", ds_random)
print("Độ dài của list_ sau khi thêm:", len(list_))
#d.Tính tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
ds_ngay = {"mon", "tue", "sat", "sun"} 
sale_value = 0 
for ngay, gtri in list_:
    if ngay in ds_ngay:
        sale_value += gtri 
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", sale_value)